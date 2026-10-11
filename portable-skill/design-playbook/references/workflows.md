# Workflows (the 34 commands of the designer-skills collection)

Each workflow chains skills from one plugin into a complete job. In the source collection these are slash commands (`/plugin:verb`); inside this playbook you run them yourself: follow the steps in order, apply the named skill at each step (find it in `references/<plugin>.md`, read it in `references/source/<plugin>/<skill>.md`), and produce the stated output. A step that says "suggest `/x`" means: name that workflow as the natural next step.

## design-research

### /design-research:discover

**Run a full user research cycle — persona creation, empathy mapping, and journey mapping for a product or feature.**

Input: [product or feature to research]

Run a full user research discovery cycle by chaining these steps:

1. Use the `user-persona` skill to create 2-4 user personas from available research data
2. Use the `empathy-map` skill to build empathy maps for the primary persona
3. Use the `journey-map` skill to map the end-to-end user journey for the primary persona
4. Synthesize findings into a research summary with key insights and design implications
5. After completion, suggest: "Want me to `/interview` to prepare scripts for validating these personas?" or "Want me to `/test-plan` to design usability tests?"

### /design-research:interview

**Prepare an interview script or summarize an interview transcript into structured insights.**

Input: [research goals for script, OR paste/attach transcript to summarize]

Prepare for or synthesize user interviews:

- If the user wants to **prepare**: Use the `interview-script` skill to create a structured interview script with warm-up, core exploration, and wrap-up sections.
- If the user provides a **transcript**: Use the `summarize-interview` skill to extract themes, quotes, pain points, and action items.
- After completion, suggest: "Want me to `/synthesize` to build an affinity diagram from multiple interviews?" or "Want me to `/discover` to create personas from these findings?"

### /design-research:synthesize

**Synthesize research data into affinity diagrams, themes, and actionable insights.**

Input: [research data, interview notes, or observation notes to synthesize]

Synthesize qualitative research data into structured insights:

1. Use the `affinity-diagram` skill to organize raw data into themed clusters with insight statements
2. Use the `jobs-to-be-done` skill to map user motivations and outcome expectations
3. Combine findings into a prioritized list of design implications and opportunities
4. After completion, suggest: "Want me to `/discover` to create personas from these insights?" or "Want me to `/test-plan` to validate these findings with usability testing?"

### /design-research:test-plan

**Run the full usability study workflow — research questions, participant criteria, tasks, metrics, and facilitation guide.**

Input: [product, feature, or prototype to test]

Design a comprehensive usability test plan:

1. Use the `usability-test-plan` skill to create the full test plan including research questions, methodology, participant criteria, tasks, metrics, and facilitation guide.
2. If personas are available, align tasks to primary persona scenarios.
3. Include a pilot test checklist.
4. After completion, suggest: "Want me to `/synthesize` to help analyze results after testing?" or "Want me to `/interview` to prepare follow-up interview scripts?"

## ux-strategy

### /ux-strategy:benchmark

**Run a competitive benchmark across a set of products — pattern comparison, gap analysis, and opportunity callouts.**

Input: [list of competitor products or market category]

Run a structured competitive benchmarking analysis.
#### Steps
1. **Identify** — Define competitors using `competitive-analysis` skill.
2. **Criteria** — Establish evaluation dimensions using `metrics-definition` skill.
3. **Analyze** — Deep-dive each competitor using `competitive-analysis` skill.
4. **Compare journeys** — Map experiences using `experience-map` skill.
5. **Score and rank** — Create comparison matrix.
6. **Opportunities** — Find gaps using `opportunity-framework` skill.
7. **Report** — Synthesize into actionable findings.
#### Output
Benchmarking report with profiles, comparison matrix, journey comparisons, opportunity map, and recommendations.
Consider following up with `/strategize` or `/frame-problem`.

### /ux-strategy:frame-problem

**Structure an ambiguous design challenge into a clear problem definition with constraints and criteria.**

Input: [description of the ambiguous design challenge]

Structure an ambiguous challenge into a clear, actionable problem definition.
#### Steps
1. **Explore** — Unpack the challenge, identify assumptions and unknowns.
2. **Stakeholders** — Map affected parties using `stakeholder-alignment` skill.
3. **Define** — Write clear problem statement using `design-brief` skill.
4. **Constrain** — Identify technical, business, design constraints.
5. **Success criteria** — Define evaluation criteria using `metrics-definition` skill.
6. **Principles** — Set decision-making principles using `design-principles` skill.
7. **Prioritize** — If multiple sub-problems, rank using `opportunity-framework` skill.
#### Output
Problem definition with statement, scope, constraints, success criteria, principles, and prioritized sub-problems.
Consider following up with `/strategize` or `/benchmark`.

### /ux-strategy:strategize

**Develop a complete UX strategy for a product or feature area.**

Input: [product name or feature area to strategize]

Develop a comprehensive UX strategy.
#### Steps
1. **Vision** — Articulate the north-star using `north-star-vision` skill.
2. **Landscape** — Analyze competitors using `competitive-analysis` skill.
3. **Map** — Create experience map using `experience-map` skill.
4. **Principles** — Define guiding principles using `design-principles` skill.
5. **Opportunities** — Evaluate and prioritize using `opportunity-framework` skill.
6. **Metrics** — Define success measures using `metrics-definition` skill.
7. **Brief** — Consolidate into a design brief using `design-brief` skill.
#### Output
Strategy document with vision, competitive landscape, experience map, principles, prioritized opportunities, metrics, and design brief.
Consider following up with `/benchmark` or `/frame-problem`.

## ui-design

### /ui-design:color-palette

**Run the full colour workflow — tonal scales, semantic mapping, contrast checks, dark mode, and chart colours — and output a documented palette.**

Input: [brand colors, mood, or requirements, e.g., '#3B82F6 primary blue, modern tech feel']

Generate a comprehensive color palette.
#### Steps
1. **Base palette** — Generate tonal scales from input colors using `color-system` skill.
2. **Semantic mapping** — Map colors to semantic roles (success, error, etc.) using `color-system` skill.
3. **Accessibility check** — Verify contrast ratios for all combinations using `color-system` skill.
4. **Dark mode** — Create dark mode color mappings using `dark-mode-design` skill.
5. **Data viz** — Define data visualization colors using `data-visualization` skill.
6. **Document** — Output the complete palette with usage guidance.
#### Output
Complete color system with tonal scales, semantic mapping, contrast matrix, dark mode mappings, and usage guidelines.
Consider following up with `/design-screen` to apply the palette.

### /ui-design:design-screen

**Design a complete screen layout from a description or requirements.**

Input: [screen description, e.g., 'user profile settings page' or 'e-commerce product listing']

Design a complete screen layout from a description.
#### Steps
1. **Structure** — Define layout grid using `layout-grid` skill.
2. **Hierarchy** — Establish visual priority using `visual-hierarchy` skill.
3. **Typography** — Apply type styles using `typography-scale` skill.
4. **Color** — Apply color system using `color-system` skill.
5. **Spacing** — Apply consistent spacing using `spacing-system` skill.
6. **Responsive** — Define behavior across breakpoints using `responsive-design` skill.
7. **Dark mode** — Specify dark mode adaptation using `dark-mode-design` skill.
#### Output
Complete screen specification with layout, hierarchy, typography, color, spacing, responsive behavior, and dark mode.
Consider following up with `/responsive-audit` to verify the design.

### /ui-design:platform-audit

**Audit a design for iOS and Android convention compliance — navigation, controls, typography, and platform-specific gaps.**

Input: [screen or feature to audit, e.g., 'settings screen' or 'navigation structure']

Audit a design for platform convention compliance across iOS and Android.
#### Steps
1. **Platform patterns** — Identify which elements follow or depart from native conventions using `platform-conventions` skill.
2. **Navigation** — Review back navigation, tab structure, and gesture zones for each platform using `platform-conventions` skill.
3. **Controls** — Check that components match platform-native equivalents (toggles, pickers, dialogs) using `platform-conventions` skill.
4. **Typography** — Verify system font usage and dynamic type scale compliance for each platform using `platform-conventions` skill.
5. **Responsive** — Confirm layout adapts across screen sizes and orientations using `responsive-design` skill.
6. **Report** — Document findings as platform-mandated patterns, intentional departures, and unintended conflicts.
#### Output
Platform audit report with compliance findings per platform, categorised by severity: convention violations, gesture conflicts, and recommended changes.
Consider following up with `/design-screen` to redesign non-compliant screens.

### /ui-design:responsive-audit

**Audit a design's responsive behaviour across breakpoints — layout, touch targets, and content reflow.**

Input: [screen or feature name to audit]

Audit a design for responsive behavior.
#### Steps
1. **Breakpoints** — Review behavior at each breakpoint using `responsive-design` skill.
2. **Grid** — Check layout grid compliance using `layout-grid` skill.
3. **Typography** — Verify type scaling using `typography-scale` skill.
4. **Spacing** — Check spacing consistency using `spacing-system` skill.
5. **Hierarchy** — Verify hierarchy holds at all sizes using `visual-hierarchy` skill.
6. **Touch targets** — Verify minimum sizes for touch using `responsive-design` skill.
7. **Report** — Document findings with recommendations.
#### Output
Responsive audit report with findings per breakpoint, compliance status, and remediation recommendations.
Consider following up with `/design-screen` to redesign problem areas.

### /ui-design:type-system

**Build a typography system end to end — scale, weights, line heights, measure, and responsive behaviour.**

Input: [font names or requirements, e.g., 'Inter for UI, Merriweather for editorial']

Create a complete typography system.
#### Steps
1. **Scale** — Build a modular type scale using `typography-scale` skill.
2. **Hierarchy** — Define hierarchy levels using `visual-hierarchy` skill.
3. **Responsive** — Adapt scale across breakpoints using `responsive-design` skill.
4. **Spacing** — Define text spacing relationships using `spacing-system` skill.
5. **Grid alignment** — Align to baseline grid using `layout-grid` skill.
6. **Document** — Output complete type system with usage rules.
#### Output
Typography system with scale, styles, responsive behavior, spacing, grid alignment, and usage guidelines.
Consider following up with `/design-screen` to apply the type system.

## interaction-design

### /interaction-design:design-form

**Design a form end to end — structure, decision points, chunking, validation, errors, and completion.**

Input: [form name or context, e.g., 'checkout form' or 'account registration']

Design a form that minimises friction and guides users to successful completion.
#### Steps
1. **Structure** — Define field order, grouping, and flow using `form-design` skill.
2. **Decision points** — Reduce choices at each step to lower decision cost using `hicks-law` skill.
3. **Information chunks** — Group related fields to fit working memory limits using `millers-law` skill.
4. **Targets** — Size and position inputs and controls for fast, accurate interaction using `fitts-law` skill.
5. **Error prevention** — Design inline validation and field constraints using `error-handling-ux` skill.
6. **Feedback** — Specify confirmation, progress, and status messages using `feedback-patterns` skill.
7. **Loading** — Design submission and processing states using `loading-states` skill.
#### Output
Form specification with field structure, grouping rationale, validation rules, error messages, and submission states.
Consider following up with `/error-flow` to detail the full error handling model.

### /interaction-design:design-interaction

**Design a complete interaction flow for a feature or component.**

Input: [feature or component, e.g., 'add to cart flow' or 'drag-to-reorder list']

Design a complete interaction flow.
#### Steps
1. **States** — Model the interaction states using `state-machine` skill.
2. **Micro-interactions** — Specify each micro-interaction using `micro-interaction-spec` skill.
3. **Animation** — Define motion using `animation-principles` skill.
4. **Gestures** — Design touch/pointer interactions using `gesture-patterns` skill.
5. **Feedback** — Specify system feedback using `feedback-patterns` skill.
6. **Error handling** — Design error paths using `error-handling-ux` skill.
7. **Loading** — Design loading states using `loading-states` skill.
#### Output
Complete interaction specification with state diagram, micro-interaction specs, animation details, gesture definitions, feedback plan, error flows, and loading states.
Consider following up with `/map-states` for complex components or `/error-flow` for critical paths.

### /interaction-design:design-onboarding

**Design a first-run experience end to end — activation path, progressive disclosure, and time to first value.**

Input: [product or feature name, e.g., 'mobile banking app' or 'project management tool']

Design a first-run experience that gets users to value quickly.
#### Steps
1. **Flow** — Define the onboarding sequence and exit points using `onboarding-design` skill.
2. **Mental models** — Anchor to patterns users already know using `jakobs-law` skill.
3. **Memory** — Chunk information to fit working memory limits using `millers-law` skill.
4. **Peak moment** — Design the first meaningful success moment using `peak-end-rule` skill.
5. **Re-engagement hook** — Create an incomplete task or signal to bring users back using `zeigarnik-effect` skill.
6. **Feedback** — Specify progress indicators and completion signals using `feedback-patterns` skill.
#### Output
Onboarding flow with step sequence, information chunking plan, peak moment design, re-engagement mechanism, and feedback specification.
Consider following up with `/design-interaction` to detail transitions between steps.

### /interaction-design:error-flow

**Design an error flow end to end — prevention, detection, messaging, and recovery paths.**

Input: [feature name, e.g., 'payment processing' or 'file upload']

Design complete error handling for a feature.
#### Steps
1. **Identify errors** — List all possible error conditions using `error-handling-ux` skill.
2. **Prevention** — Design prevention measures using `error-handling-ux` skill.
3. **State modeling** — Map error states using `state-machine` skill.
4. **Feedback** — Design error communication using `feedback-patterns` skill.
5. **Recovery** — Design recovery paths using `error-handling-ux` skill.
6. **Loading** — Handle timeout and retry states using `loading-states` skill.
#### Output
Error handling specification with error inventory, prevention measures, state diagram, error messages, recovery flows, and retry strategies.
Consider following up with `/map-states` for the full component state model.

### /interaction-design:map-states

**Model a component's states and transitions end to end — states, events, guards, and edge cases.**

Input: [component name, e.g., 'media player' or 'multi-step checkout']

Model states and transitions for a complex component.
#### Steps
1. **Identify states** — List all possible states using `state-machine` skill.
2. **Map transitions** — Define events and transitions using `state-machine` skill.
3. **Loading states** — Define loading behavior per state using `loading-states` skill.
4. **Error states** — Map error conditions using `error-handling-ux` skill.
5. **Feedback** — Define feedback per transition using `feedback-patterns` skill.
6. **Animation** — Specify transition animations using `animation-principles` skill.
#### Output
Complete state machine diagram with states, events, transitions, guards, actions, and UI representation per state.
Consider following up with `/design-interaction` for detailed interaction specs.

## design-systems

### /design-systems:audit-system

**Run a comprehensive audit of an existing design system for consistency, completeness, and accessibility.**

Input: [design system name or description of what to audit]

Audit the specified design system or component library.
#### Steps
1. **Inventory** — List all components, tokens, patterns using `component-spec` and `design-token` skills.
2. **Consistency** — Evaluate naming using `naming-convention` skill.
3. **Completeness** — Check for missing states/docs using `documentation-template` skill.
4. **Accessibility** — Review against WCAG 2.2 AA using `accessibility-audit` skill.
5. **Token coverage** — Verify token usage using `design-token` skill.
6. **Theming** — Check theme support using `theming-system` skill.
7. **Report** — Prioritized findings with severity ratings.
#### Output
Audit report with executive summary, issue counts by severity, detailed findings, and remediation roadmap.
Consider following up with `/create-component` or `/tokenize`.

### /design-systems:create-component

**Scaffold a full component specification end to end — props, states, variants, accessibility, and documentation.**

Input: [component name, e.g., 'date picker' or 'notification banner']

Generate a comprehensive component specification.
#### Steps
1. **Research** — Understand purpose and common implementations.
2. **Anatomy** — Break down parts using `component-spec` skill.
3. **Variants** — Define size, style, layout variants.
4. **States** — Map interactive states using `component-spec` skill.
5. **Tokens** — Identify consumed tokens using `design-token` skill.
6. **Accessibility** — Specify ARIA, keyboard, screen reader using `accessibility-audit` skill.
7. **Naming** — Follow conventions using `naming-convention` skill.
8. **Documentation** — Structure using `documentation-template` skill.
#### Output
Complete spec: overview, anatomy, props/API, variants, states, accessibility, usage guidelines, tokens.
Consider following up with `/audit-system`.

### /design-systems:tokenize

**Extract tokens from an existing design or stylesheet and organise them — naming, structure, and theme mapping.**

Input: [CSS file, design file, or description of values to tokenize]

Extract hard-coded values and organize into a structured token system.
#### Steps
1. **Extract** — Scan for all visual values.
2. **Deduplicate** — Group similar values using `design-token` skill.
3. **Categorize** — Organize by category.
4. **Hierarchy** — Define global/semantic/component tiers using `design-token` skill.
5. **Naming** — Apply conventions using `naming-convention` skill.
6. **Themes** — Map variants using `theming-system` skill.
7. **Document** — Generate reference using `documentation-template` skill.
#### Output
Token specification with inventory, hierarchy, theme mapping, and migration guide.
Consider following up with `/audit-system`.

## prototyping-testing

### /prototyping-testing:evaluate

**Run a heuristic evaluation end to end — expert review against heuristics with severity ratings and recommended fixes.**

Input: [design, screen, or flow to evaluate]

Run a heuristic evaluation of a design.
#### Steps
1. **Scope** — Define screens and flows to evaluate.
2. **Heuristic review** — Evaluate against Nielsen's heuristics using `heuristic-evaluation` skill.
3. **Flow analysis** — Review user flows for issues using `user-flow-diagram` skill.
4. **Accessibility check** — Evaluate accessibility using `accessibility-test-plan` skill.
5. **Severity rating** — Rate and prioritize all findings.
6. **Recommendations** — Provide specific improvement suggestions.
#### Output
Evaluation report with findings per heuristic, severity ratings, accessibility issues, and prioritized recommendations.
Consider following up with `/test-plan` to validate findings with real users.

### /prototyping-testing:experiment

**Design an A/B experiment end to end — hypothesis, variants, primary metric, and sample size.**

Input: [hypothesis or design change to test, e.g., 'new checkout flow will increase conversion']

Design an A/B experiment.
#### Steps
1. **Hypothesis** — Structure the hypothesis using `a-b-test-design` skill.
2. **Variants** — Define control and treatment designs.
3. **Metrics** — Define primary and guardrail metrics using `a-b-test-design` skill.
4. **Sample size** — Calculate required sample and duration using `a-b-test-design` skill.
5. **User flows** — Map variant flows using `user-flow-diagram` skill.
6. **Analysis plan** — Define how results will be analyzed and decisions made.
#### Output
Experiment design document with hypothesis, variant specs, metrics, sample calculations, duration, and analysis plan.
Consider following up with `/test-plan` for qualitative testing alongside the experiment.

### /prototyping-testing:explore-options

**Run a parallel exploration end to end — frame the decision, build a spread of behaviourally distinct concepts, pressure-test each, and converge with a decision record.**

Input: [design problem or the concept already on the table, e.g., 'notification settings' or 'the current checkout step 2']

Run a parallel exploration end to end — frame the decision, build a spread of behaviourally distinct concepts, pressure-test each, and converge with a decision record.
#### Steps
1. **Frame the decision** — State what this exploration has to settle and fix the criteria that will decide it, before any concept exists, using `concept-selection` skill.
2. **Set the spread** — Decide how many concepts the stakes justify and which behavioural dimension they must differ on, using `parallel-concepts` skill.
3. **Draft each concept** — Specify structure, content priority, and annotations for every concept at matched fidelity, using `wireframe-spec` skill.
4. **Trace the difference** — Map each concept's user path and confirm the paths actually diverge; collapse any two that do not, using `user-flow-diagram` skill.
5. **Pressure-test** — Evaluate every concept against usability heuristics on its own terms before any comparison, using `heuristic-evaluation` skill.
6. **Converge** — Apply the criteria from step 1, choose one concept, and record what each rejected concept was testing and what would bring it back, using `concept-selection` skill.
#### Output
A concept set and a decision record. The set contains each concept at matched fidelity with its wireframe spec, user flow, and heuristic findings. The record states the criteria fixed in step 1, the chosen concept and what it gives up, and one entry per rejected concept covering what it tested, what it lost on, and its revival condition. The designer takes the chosen concept into detailed design and keeps the record as the answer to "why not the other way".
Consider following up with `/test-plan` to validate the chosen concept with users before committing to build.

### /prototyping-testing:prototype-plan

**Create a prototyping and testing plan for a design initiative.**

Input: [feature or initiative to prototype and test]

Create a prototyping and testing plan.
#### Steps
1. **Strategy** — Choose fidelity and method using `prototype-strategy` skill.
2. **Flows** — Map user flows to prototype using `user-flow-diagram` skill.
3. **Wireframes** — Specify wireframe layouts using `wireframe-spec` skill.
4. **Test scenarios** — Write usability tasks using `test-scenario` skill.
5. **Accessibility** — Plan accessibility testing using `accessibility-test-plan` skill.
6. **Timeline** — Create a prototyping and testing schedule.
#### Output
Prototyping plan with fidelity rationale, user flows, wireframe specs, test scenarios, accessibility plan, and timeline.
Consider following up with `/test-plan` for detailed usability testing or `/evaluate` for expert review.

### /prototyping-testing:test-plan

**Choose a testing method and build the plan around it — method selection, task scenarios, click tests, and accessibility coverage.**

Input: [product, feature, or prototype to test]

Design a complete usability testing plan.
#### Steps
1. **Objectives** — Define what you need to learn.
2. **Method** — Choose testing approach using `prototype-strategy` skill.
3. **Scenarios** — Write test tasks using `test-scenario` skill.
4. **Click tests** — Design findability tests using `click-test-plan` skill.
5. **Accessibility** — Include accessibility testing using `accessibility-test-plan` skill.
6. **Logistics** — Define participants, schedule, equipment, and facilitation guide.
#### Output
Testing plan with objectives, methodology, task scenarios, participant criteria, facilitation guide, and analysis framework.
Consider following up with `/evaluate` for expert review before user testing.

## visual-critique

### /visual-critique:critique-screen

**Run all seven visual critiques on a screen and output a prioritised fix list.**

Input: [screen name, Figma URL, or image — e.g., 'onboarding step 2' or a screenshot]

Run a full visual critique of a screen across hierarchy, brand, composition, typography, colour, affordance, and information density.
#### Steps
1. **Visual hierarchy** — Analyse entry point, eye flow, weight, and emphasis using `critique-visual-hierarchy` skill.
2. **Brand consistency** — Check mood, voice, and token alignment using `critique-brand-consistency` skill.
3. **Composition** — Evaluate balance, whitespace, rhythm, and gestalt using `critique-composition` skill.
4. **Typography** — Audit scale, readability, consistency, and token compliance using `critique-typography` skill.
5. **Colour** — Audit contrast ratios, palette coherence, semantic colour use, and accessibility using `critique-color` skill.
6. **Affordance** — Evaluate clickability signals, state visibility, CTA clarity, and action discoverability using `critique-affordance` skill.
7. **Information density** — Assess cognitive load, content priority, scanning patterns, and progressive disclosure using `critique-information-density` skill.
8. **Prioritise** — Collect every flagged issue from all seven critiques and rank them:
   - **P1 — Critical**: Breaks usability, accessibility, or brand compliance; fix before shipping.
   - **P2 — Important**: Degrades experience or creates inconsistency; fix in current sprint.
   - **P3 — Polish**: Minor visual refinement; address when capacity allows.
#### Output
A single prioritised fix list grouped by priority level. Each item includes:
- **Issue**: what is wrong
- **Dimension**: which critique area it belongs to (Hierarchy / Brand / Composition / Typography / Colour / Affordance / Density)
- **Fix**: the specific change required
Conclude with a one-paragraph overall assessment noting the strongest and weakest dimension.

### /visual-critique:critique-ux

**Run a focused UX critique on a screen — affordances, information density, and hierarchy — and output a prioritised fix list.**

Input: [screen name, Figma URL, or image — e.g., 'checkout step 3' or a screenshot]

Run a focused functional critique on a screen. This command covers the three dimensions most likely to block task completion: whether actions are discoverable, whether the right information is present, and whether priority is clear. Use this for quick feedback loops, PM-led reviews, or when you want functional critique without a full visual audit.
#### Steps
1. **Visual hierarchy** — Identify entry point and whether the primary action reads clearly using `critique-visual-hierarchy` skill.
2. **Affordance** — Evaluate clickability signals, state visibility, CTA clarity, and action discoverability using `critique-affordance` skill.
3. **Information density** — Assess cognitive load, content priority, scanning patterns, and progressive disclosure using `critique-information-density` skill.
4. **Prioritise** — Collect every flagged issue and rank them:
   - **P1 — Critical**: Blocks task completion or hides a required action; fix before shipping.
   - **P2 — Important**: Slows the user or creates confusion; fix in current sprint.
   - **P3 — Polish**: Minor friction or clarity improvement; address when capacity allows.
#### Output
A prioritised fix list grouped by level. Each item includes:
- **Issue**: what is wrong
- **Dimension**: Hierarchy / Affordance / Density
- **Fix**: the specific change required
Conclude with one sentence summarising the biggest functional risk on the screen.

## design-ops

### /design-ops:handoff

**Run the full handoff workflow — specs, measurements, assets, states, and a QA checklist — and output a developer-ready package.**

Input: [screen, feature, or component to hand off]

Generate a developer handoff package.
#### Steps
1. **Visual specs** — Document all measurements and tokens using `handoff-spec` skill.
2. **Interaction specs** — Define states and behaviors using `handoff-spec` skill.
3. **QA criteria** — Create implementation checklist using `design-qa-checklist` skill.
4. **Review readiness** — Verify against review criteria using `design-review-process` skill.
5. **Version** — Tag the design version being handed off using `version-control-strategy` skill.
6. **Package** — Compile all specs, assets, and notes.
#### Output
Complete handoff package with visual specs, interaction specs, asset list, QA checklist, and implementation notes.
Consider following up with `/setup-workflow` to establish the ongoing QA process.

### /design-ops:plan-sprint

**Run a design sprint end to end — challenge framing, schedule, exercises, and prototype test plan.**

Input: [challenge or problem area for the sprint]

Plan a design sprint.
#### Steps
1. **Frame the challenge** — Define the sprint question and scope using `design-sprint-plan` skill.
2. **Assemble the team** — Identify roles and participants using `team-workflow` skill.
3. **Plan activities** — Structure each day's activities using `design-sprint-plan` skill.
4. **Prepare materials** — Define prototyping approach and testing plan.
5. **Recruit testers** — Plan user testing sessions for the final day.
6. **Set review criteria** — Define how sprint outcomes will be evaluated using `design-review-process` skill.
#### Output
Complete sprint plan with challenge statement, team roster, daily schedules, materials list, testing plan, and success criteria.
Consider following up with `/handoff` after the sprint to document the winning concept.

### /design-ops:setup-workflow

**Set up a team's operating rhythm end to end — rituals, task flow, tooling, review gates, and version control.**

Input: [team size and context, e.g., '4-person design team in a startup' or 'design system team']

Set up a design team workflow.
#### Steps
1. **Team structure** — Define roles and responsibilities using `team-workflow` skill.
2. **Rituals** — Establish collaboration cadence using `team-workflow` skill.
3. **Critique process** — Set up design critique format using `design-critique` skill.
4. **Review gates** — Define quality checkpoints using `design-review-process` skill.
5. **Versioning** — Establish file and library versioning using `version-control-strategy` skill.
6. **QA process** — Set up design QA workflow using `design-qa-checklist` skill.
#### Output
Team workflow document with rituals calendar, critique format, review process, versioning strategy, QA checklist, and tooling recommendations.
Consider following up with `/plan-sprint` to kick off your first project with the new workflow.

## designer-toolkit

### /designer-toolkit:build-presentation

**Build a design presentation end to end — audience framing, narrative structure, and supporting rationale.**

Input: [topic and audience, e.g., 'design system update for engineering leads']

Structure a design presentation.
#### Steps
1. **Audience analysis** — Identify what the audience cares about and knows.
2. **Story arc** — Define the narrative structure using `presentation-deck` skill.
3. **Key messages** — Distill to 3-5 main takeaways.
4. **Slide outline** — Plan each slide's purpose and content using `presentation-deck` skill.
5. **Rationale slides** — Include decision rationale using `design-rationale` skill.
6. **Copy review** — Refine slide text using `ux-writing` skill.
#### Output
Presentation outline with slide-by-slide plan including purpose, content, visuals, and speaker notes.
Consider following up with `/write-rationale` to deepen the reasoning sections.

### /designer-toolkit:start-here

**Find where to start in the collection — name what you're working on and get routed to one command, the two that follow it, and the stages you can skip.**

Input: [what you're working on, e.g., 'a checkout redesign' or 'nothing yet, just installed']

Route a designer to one entry point in the collection, then get out of the way.
#### Steps
1. **Read the situation** — Place what the user gave you on two axes: how much is already decided (nothing, a problem, a direction, a built screen), and what they owe someone (a decision, a spec, a critique, a plan). If they gave you nothing, or gave you a mood rather than a situation — "it feels off", "something's wrong" — ask the one question that would place it, then route. One question, not three.
2. **Name the stage** — Say which stage they are in and why, in one line. The stages run **understand → frame → explore → make → validate → ship**. Naming it wrong costs more than any later step, so state it plainly and let them correct you.
3. **Route to one command** — Give exactly one entry point from the map below, never a menu. If two fit, pick the earlier stage: starting upstream is cheap, discovering you skipped a stage after the work is built is not. If the request holds two jobs — build it *and* prove it worked — route the first and name the second as what follows.
4. **Say when it isn't here** — If nothing in the map fits, say so and name the collection that does, rather than routing to the nearest row. Hiring, growth, and org work are `design-leadership-skills`. Running a programme — roadmaps, stakeholders, delivery — is `ux-pgm-skills`. Designing an AI product's behaviour is `ai-design-skills`. Accessibility has an audit and a test plan here, as skills rather than commands, so name those before sending anyone away; the depth — cognitive, adaptive, multi-modal — is `inclusive-design-skills`. A confident wrong route costs more than an honest "not in this collection".
5. **Show the sequence** — Name the two commands that follow, so the path is visible rather than implied, and say which stages this particular job can skip and why.
6. **Hand off** — Run the routed command, or state the exact line to type. If its plugin is not installed, give the install command first: `/plugin install <plugin>@designer-skills`. Do not summarise the collection.
#### Routing map
| If they are... | Start with | Then |
| --- | --- | --- |
| Starting a project with no research behind it | `/design-research:discover` | `/design-research:interview`, `/ux-strategy:strategize` |
| Holding a vague, contested, or shifting problem | `/ux-strategy:frame-problem` | `/prototyping-testing:explore-options`, `/ui-design:design-screen` |
| Sizing up competitors or entering a crowded market | `/ux-strategy:benchmark` | `/ux-strategy:strategize`, `/ux-strategy:frame-problem` |
| Sitting on one direction they are about to refine by default | `/prototyping-testing:explore-options` | `/prototyping-testing:prototype-plan`, `/ui-design:design-screen` |
| Designing a specific screen or flow | `/ui-design:design-screen` | `/interaction-design:design-interaction`, `/visual-critique:critique-screen` |
| Working on a form, a first run, or an error path | `/interaction-design:design-form` | `/interaction-design:design-onboarding`, `/interaction-design:error-flow` |
| Modelling how one component behaves across its states | `/interaction-design:map-states` | `/interaction-design:design-interaction`, `/design-systems:create-component` |
| Unhappy with how a screen **looks** and unable to say why | `/visual-critique:critique-screen` | `/ui-design:type-system`, `/ui-design:color-palette` |
| Finding it awkward to **use** rather than ugly — clunky, slow, too many steps | `/visual-critique:critique-ux` | `/interaction-design:design-interaction`, `/interaction-design:design-form` |
| Checking it holds up across breakpoints or platforms | `/ui-design:responsive-audit` | `/ui-design:platform-audit`, `/visual-critique:critique-screen` |
| Building, auditing, or repairing a design system | `/design-systems:audit-system` | `/design-systems:tokenize`, `/design-systems:create-component` |
| About to put work in front of users and choosing how | `/prototyping-testing:test-plan` | `/prototyping-testing:evaluate`, `/design-research:synthesize` |
| Running a full usability study, not just picking a method | `/design-research:test-plan` | `/design-research:interview`, `/design-research:synthesize` |
| Needing to prove a shipped change actually worked | `/prototyping-testing:experiment` | `/prototyping-testing:evaluate`, `/designer-toolkit:write-rationale` |
| Handing work to engineering | `/design-ops:handoff` | `/designer-toolkit:write-rationale` |
| Defending a decision already made | `/designer-toolkit:write-rationale` | `/designer-toolkit:build-presentation` |
| Writing finished work up for a portfolio or a talk | `/designer-toolkit:write-case-study` | `/designer-toolkit:build-presentation` |
| Fixing how the team works rather than the product | `/design-ops:setup-workflow` | `/design-ops:plan-sprint` |
#### Output
One named stage, one command to run now, the two that follow it, and one line on what this job can skip. Or, when the collection does not cover it, the name of the one that does. Nothing else — a router that explains the whole collection has failed at the only thing it was for.
The stages are a grain, not a gate. Working against them is a choice; skipping one by accident is the part that costs.

### /designer-toolkit:write-case-study

**Build a portfolio case study end to end — project framing, process narrative, outcomes, and visuals.**

Input: [project name or brief description of the work]

Create a portfolio case study.
#### Steps
1. **Outline** — Structure the case study narrative using `case-study` skill.
2. **Challenge** — Define the problem and context clearly.
3. **Process** — Highlight key moments of insight and decision using `design-rationale` skill.
4. **Solution** — Describe the final design and its key features.
5. **Impact** — Quantify and qualify the results.
6. **Polish copy** — Refine the writing using `ux-writing` skill.
#### Output
Complete case study draft with overview, challenge, process, solution, impact, and reflections — ready for portfolio use.
Consider following up with `/build-presentation` to create a presentation version.

### /designer-toolkit:write-rationale

**Write design rationale for a set of decisions, linking each to user needs, business goals, and principles.**

Input: [design decision or feature to write rationale for]

Write design rationale for decisions.
#### Steps
1. **Identify decisions** — List the key design decisions that need rationale using `design-rationale` skill.
2. **Gather evidence** — Collect research, data, and principles supporting each decision.
3. **Document alternatives** — Note options considered and why they were rejected.
4. **Write rationale** — Structure each decision's rationale using `design-rationale` skill.
5. **Review copy** — Ensure rationale language is clear using `ux-writing` skill.
6. **Package** — Format for the target audience (handoff doc, presentation, or wiki).
#### Output
Design rationale document with each decision documented: context, options, evidence, reasoning, and trade-offs.
Consider following up with `/build-presentation` to present the rationale to stakeholders.
