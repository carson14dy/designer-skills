---
name: design-playbook
description: "The designer-skills collection (111 skills, 34 workflows) as one portable playbook for designing and reviewing apps and websites: research, strategy, UI, interaction, design systems, testing, critique, handoff. Use it whenever the user asks you to design, lay out, build, restyle, or critique anything people will see on a screen (a landing page, dashboard, app screen, signup, checkout, settings, navigation, form, onboarding, empty state, error message, colour palette, type scale, component, or design system), even if they never say the word design, and whenever they ask for personas, interview scripts, usability or A/B tests, concept exploration, handoff specs, or design rationale. Read the matching skills in references/ before producing anything."
license: MIT
---
# Design Playbook

You are working with the judgment of a full design practice, written so an agent can apply it literally. This playbook is the design-practice collection of the Designer Skills suite by MC Dean (Owl-Listener/designer-skills, MIT), compressed into one skill: 9 plugins, 111 skills (nouns, domain knowledge) and 34 workflows (verbs, pipelines that chain skills). Treat it as the standard you are held to, not optional reading.

## How to work

1. **Route first.** Place the request on the grain **understand → frame → explore → make → validate → ship**. Name the stage in one line and let the user correct you. If two stages fit, start with the earlier one: starting upstream is cheap, discovering a skipped stage after the build is not. If the request holds two jobs (build it and prove it worked), do the first and name the second as what follows.
2. **Open the source skills before producing anything.** This file carries the numbers; the judgment lives in `references/source/`: the tables, the decision heuristics, and the "do not" lines that separate a competent answer from an expert one. Runs that skipped this step produced flatter work: no per-dimension ratings, type sizes left vague, conventions missed. The harness tells you this skill's base directory when it loads; every path below is relative to it. Read the whole reading list for the task type (3 to 7 short files, about 2 minutes), then the plugin index `references/<plugin>.md` if the task touches skills not listed.
3. **Run the workflow.** `references/workflows.md` holds all 34 pipelines. Follow the steps in order, name the skill driving each step in your output, and produce the stated artifact.
4. **Close every build with two sections inside the deliverable: the self-critique and the rationale.** A deliverable without them is unfinished, whatever else it contains. Before writing them read `references/source/designer-toolkit/design-rationale.md` and the seven `references/source/visual-critique/critique-*.md` files.
   - Self-critique: the seven dimensions (hierarchy, brand, composition, typography, colour, affordance, information density), each rated pass, minor issue, or major issue (or "not assessable" with the reason). For each finding: Observation (neutral), Problem (why it matters), Fix (specific). Then every fix under P1 critical, P2 important, P3 polish, in the order it should be done, so the list is itself the plan.
   - Rationale: decision, context, options considered, evidence, reasoning, trade-offs, validation plan. Write it as you decide, not afterwards.

| Stage | What it covers | Read |
| --- | --- | --- |
| Understand | Personas, empathy and journey maps, interviews, surveys, usability studies, analytics, qual vs quant conflicts | `references/design-research.md` |
| Frame | Brief, north star, principles, competitive analysis, IA, content strategy, metrics, opportunity scoring, service blueprint | `references/ux-strategy.md` |
| Explore | Parallel concepts, concept selection, prototype strategy, wireframes, user flows | `references/prototyping-testing.md` |
| Make (surface) | Grid, hierarchy, type, colour, spacing, dark mode, responsive, data viz, Gestalt laws, platform conventions | `references/ui-design.md` |
| Make (behaviour) | Forms, onboarding, navigation, search, errors, feedback, loading, states, motion, gestures, cognitive laws | `references/interaction-design.md` |
| Systematise | Tokens, components, naming, theming, motion system, icons, localisation, accessibility audit, governance | `references/design-systems.md` |
| Validate | Heuristic evaluation, usability and click tests, A/B design, accessibility testing | `references/prototyping-testing.md` |
| Validate (by eye) | The seven screen critiques | `references/visual-critique.md` |
| Ship | Handoff spec, QA checklist, review gates, critique facilitation, debt audit, impact reporting | `references/design-ops.md` |
| Advocate | Rationale, negotiation, presentations, case studies, UX writing, system adoption, token audit | `references/designer-toolkit.md` |

## Reading list by task type

Read every file in the matching row first. Paths are under `references/source/`. If the task spans two rows, read both.

| Task | Read first |
| --- | --- |
| A screen, page, or layout | `ui-design/layout-grid.md`, `ui-design/visual-hierarchy.md`, `ui-design/typography-scale.md`, `ui-design/spacing-system.md`, `ui-design/color-system.md`, `ui-design/responsive-design.md`, `ui-design/dark-mode-design.md` |
| A form, signup, checkout, or settings page | `interaction-design/form-design.md`, `interaction-design/error-handling-ux.md`, `interaction-design/feedback-patterns.md`, `interaction-design/hicks-law.md`, `interaction-design/millers-law.md`, `interaction-design/fitts-law.md` |
| First-run or onboarding | `interaction-design/onboarding-design.md`, `interaction-design/peak-end-rule.md`, `interaction-design/zeigarnik-effect.md`, `interaction-design/jakobs-law.md`, `interaction-design/loading-states.md`, plus the form row if there is a signup |
| A flow, component, or anything with states | `interaction-design/state-machine.md`, `interaction-design/micro-interaction-spec.md`, `interaction-design/loading-states.md`, `interaction-design/feedback-patterns.md`, `interaction-design/error-handling-ux.md`, `interaction-design/animation-principles.md` |
| Navigation or search | `interaction-design/navigation-patterns.md`, `interaction-design/search-ux.md`, `interaction-design/serial-position-effect.md`, `ux-strategy/information-architecture.md`, `ui-design/platform-conventions.md` for native apps |
| Colour, type, tokens, or a design system | `ui-design/color-system.md`, `ui-design/dark-mode-design.md`, `ui-design/typography-scale.md`, `ui-design/readable-measure.md`, `design-systems/design-token.md`, `design-systems/theming-system.md`, `ui-design/data-visualization.md` if charts |
| A critique or review of an existing screen | all seven `visual-critique/critique-*.md`, then `ui-design/visual-hierarchy.md` and `interaction-design/hicks-law.md` for the fixes |
| Research: personas, interviews, surveys, data | `design-research/user-persona.md`, `design-research/interview-script.md`, `design-research/survey-design.md`, `design-research/behavioural-analytics.md`, `design-research/qual-quant-triangulation.md`, `design-research/affinity-diagram.md` |
| Strategy: brief, principles, competitors, metrics | `ux-strategy/design-brief.md`, `ux-strategy/design-principles.md`, `ux-strategy/competitive-analysis.md`, `ux-strategy/metrics-definition.md`, `ux-strategy/opportunity-framework.md` |
| Choosing between directions | `prototyping-testing/parallel-concepts.md`, `prototyping-testing/concept-selection.md`, `prototyping-testing/prototype-strategy.md`, `prototyping-testing/wireframe-spec.md` |
| Handoff, spec, or QA | `design-ops/handoff-spec.md`, `design-ops/design-qa-checklist.md`, `designer-toolkit/design-rationale.md`, `designer-toolkit/ux-writing.md` |
| Closing any build (always) | `designer-toolkit/design-rationale.md` and all seven `visual-critique/critique-*.md` |

## Routing map

Pick exactly one entry point, never a menu. Workflows are named as in `references/workflows.md`.

| If the user is... | Start with | Then |
| --- | --- | --- |
| Starting a project with no research behind it | `/design-research:discover` | `/design-research:interview`, `/ux-strategy:strategize` |
| Holding a vague, contested, or shifting problem | `/ux-strategy:frame-problem` | `/prototyping-testing:explore-options`, `/ui-design:design-screen` |
| Sizing up competitors or entering a crowded market | `/ux-strategy:benchmark` | `/ux-strategy:strategize`, `/ux-strategy:frame-problem` |
| Sitting on one direction they are about to refine by default | `/prototyping-testing:explore-options` | `/prototyping-testing:prototype-plan`, `/ui-design:design-screen` |
| Designing a specific screen or page | `/ui-design:design-screen` | `/interaction-design:design-interaction`, `/visual-critique:critique-screen` |
| Working on a form, a first run, or an error path | `/interaction-design:design-form` | `/interaction-design:design-onboarding`, `/interaction-design:error-flow` |
| Modelling how one component behaves across its states | `/interaction-design:map-states` | `/interaction-design:design-interaction`, `/design-systems:create-component` |
| Unhappy with how a screen **looks** and unable to say why | `/visual-critique:critique-screen` | `/ui-design:type-system`, `/ui-design:color-palette` |
| Finding it awkward to **use** rather than ugly | `/visual-critique:critique-ux` | `/interaction-design:design-interaction`, `/interaction-design:design-form` |
| Checking it holds up across breakpoints or platforms | `/ui-design:responsive-audit` | `/ui-design:platform-audit`, `/visual-critique:critique-screen` |
| Building, auditing, or repairing a design system | `/design-systems:audit-system` | `/design-systems:tokenize`, `/design-systems:create-component` |
| About to put work in front of users and choosing how | `/prototyping-testing:test-plan` | `/prototyping-testing:evaluate`, `/design-research:synthesize` |
| Running a full usability study | `/design-research:test-plan` | `/design-research:interview`, `/design-research:synthesize` |
| Needing to prove a shipped change worked | `/prototyping-testing:experiment` | `/prototyping-testing:evaluate`, `/designer-toolkit:write-rationale` |
| Handing work to engineering | `/design-ops:handoff` | `/designer-toolkit:write-rationale` |
| Defending a decision already made | `/designer-toolkit:write-rationale` | `/designer-toolkit:build-presentation` |
| Writing finished work up for a portfolio or talk | `/designer-toolkit:write-case-study` | `/designer-toolkit:build-presentation` |
| Fixing how the team works rather than the product | `/design-ops:setup-workflow` | `/design-ops:plan-sprint` |

Not covered here: hiring, growth, and org work; running a programme (roadmaps, stakeholders, delivery); designing an AI product's behaviour; deep cognitive and adaptive accessibility. Say so rather than routing to the nearest row. Accessibility does have an audit (`accessibility-audit`) and a test plan (`accessibility-test-plan`) here.

## Frequently confused

| These look alike | First when | Second when |
| --- | --- | --- |
| `color-system` / `/ui-design:color-palette` | You want the reasoning | You want the workflow run and a palette out |
| `accessibility-audit` / `accessibility-test-plan` | Assessing a design or build now | Scheduling sessions with real AT users |
| `visual-hierarchy` / `critique-visual-hierarchy` | Composing new work | Judging an existing screen |
| `design-token` / `design-token-audit` | Establishing the token layer | Tokens exist and are being bypassed |
| `journey-map` / `experience-map` / `service-blueprint` | One persona, one linear path | Spans products or channels / staff and backstage are part of it |
| `usability-test-plan` / `test-scenario` | The study as a whole | The tasks inside it |
| `form-design` / `error-handling-ux` | The artifact is a form | A product-wide error strategy |
| `design-brief` / `north-star-vision` | One project's kickoff | Long-horizon aspiration |
| `design-critique` / `heuristic-evaluation` | People in the room | One expert against heuristics |
| `parallel-concepts` / `prototype-strategy` | How many directions, how they differ | Fidelity and method for building one |
| `concept-selection` / `opportunity-framework` / `a-b-test-design` | Choosing between solutions | Choosing which problem / letting traffic decide |
| `behavioural-analytics` / `metrics-definition` / `qual-quant-triangulation` | Reading data already collected | Choosing what to measure / data and research disagree |
| `hicks-law` / `millers-law` | Too many choices at once | Too much to hold in memory |
| `fitts-law` / `hicks-law` | Size and position of controls | How many controls to show |
| `jakobs-law` / `platform-conventions` | Any familiar pattern | OS-mandated iOS and Android conventions |
| `animation-principles` / `motion-system` / `micro-interaction-spec` | One animation's feel | Product-wide tokens / a full interaction spec |
| `layout-grid` / `spacing-system` / `responsive-design` | Page columns and gutters | Spacing inside components / cross-device behaviour |

## Non-negotiables (apply to every build)

**Accessibility and targets**
- Text contrast 4.5:1 minimum (AA), 7:1 AAA; 3:1 for large text (18px+ regular, 14px+ bold) and for UI components against adjacent colours. Never convey meaning by colour alone; pair with icon, label, or pattern. Test with colour-blindness simulation and in greyscale.
- Touch targets 44×44pt (Apple) / 48×48dp (Material); 24×24px minimum for pointer. Expand hit areas with padding, not visual size. Destructive actions small and distant.
- Every field has a persistent, programmatic label; placeholder text is never the only label. Errors sit directly below the field and are associated via `aria-describedby`; a multi-field error summary at top is keyboard-focusable and links to each field. Focus order follows visual order.
- Honour `prefers-reduced-motion` at the system level (replace slides, scales, and rotations with instant or opacity changes; keep spinners and progress) and `prefers-color-scheme`, with a manual toggle too. Respect Dynamic Type / sp scaling; fixed text sizes fail accessibility on both platforms.
- Visible, high-contrast focus state. Never `outline: none` without a replacement.

**Type, measure, spacing, layout**
- Body text 16px minimum (14px floor on mobile). Type scale on a ratio (1.25 major third or 1.333 perfect fourth); 4–5 sizes in regular use; ≥1.25× between scale steps; ≥1.5× size difference between hierarchy levels. Line-height 1.2 headings, 1.5 body, 1.75 long-form. Letter-spacing −0.02em large headings, 0 body, 0.05em uppercase labels. No more than two weights active on one screen.
- Measure 45–75 characters (`max-width: 65ch`, 66 ideal): 55–70 long-form, 45–65 UI body, 40–60 captions, 30–45 pull quotes. Wider measure needs more leading.
- Spacing scale from a 4px or 8px base: 2, 4, 8, 16, 24, 32, 48, 64. Never arbitrary values. Within-group spacing tighter than between-group; label tighter to its input than to the next field; less space below a heading than above it. Compact and spacious density modes shift one step.
- Grid: 4 / 8 / 12 columns (mobile / tablet / desktop); gutters 16, 24, or 32px; margins 16px mobile, 24–48px desktop; breakpoints around 375, 640/768, 1024, 1440. Baseline grid 4px or 8px. Test every breakpoint, not just the extremes.
- One primary CTA per view, filled; everything else ghost or text. If everything is emphasised, nothing is. Decide the single most important element per screen in advance. CTA labels start with a verb and name the outcome ("Save changes", not "OK").
- Use the weakest container that works: spacing before background, background before border, border before card. At most two levels of nested containers. Remove borders iteratively and check the grouping still reads.
- Tokens come in three tiers and each tier references the one below it with `var()`: raw scale (`--teal-600: #1F6F5F`), semantic alias (`--color-primary: var(--teal-600)`), component (`--button-bg: var(--color-primary)`). A semantic or component token holding a hex literal is a bug, because themes work by remapping the alias layer; test runs that wrote literals shipped a raw scale nobody used. Always ship a neutral grey scale next to the brand scale; text, borders, and surfaces draw from it.
- Dark mode is not inversion: background around #121212, elevation through lighter surfaces not shadows, desaturate primaries 10–20%, text off-white (#E0E0E0) not pure white, 4.5:1 still applies, dark variants for illustrations and logos, re-validate figure-ground and closure.
- Text never sits directly on photography without a separation layer. Modals always get a scrim.

**Motion and latency**
- Duration tokens: instant 50ms, fast 100ms, normal 200ms, moderate 300ms, slow 400ms, deliberate 600ms. Keep UI motion under 400ms; stagger related items 30–50ms; staggered sequence under 500ms, 700ms absolute ceiling. Ease-out (decelerate) entering, ease-in (accelerate) exiting, linear only for loops. Standard curve cubic-bezier(0.2, 0, 0, 1).
- Doherty threshold: respond under 400ms. Button state change within 100ms. Autocomplete within 300ms. No loading indicator for anything under 100ms; subtle indicator 100ms–1s; clear state 1–10s with progress (not just a spinner) past 3s; time estimate and background option past 10s. Skeletons beat spinners when layout is known. Never show a blank screen.
- Give 300–600ms recovery space after an error before the next prompt. Heavy news arrives slowly; good news can be instant.

**Forms, feedback, errors, states**
- Single column, top-aligned labels, field width reflects expected input length, mark optional not required, remove every optional field you can, default to the most common answer. Radios for ≤5 options, select for 6+, checkboxes for multi-select, never freeform text for structured dates, show/hide toggle on passwords, masking for phone and card numbers.
- Validate on blur, not per keystroke. Error message says what happened and how to fix it ("Email address must include @"), never blames the user, never "Something went wrong". Preserve input on error. Review step before submission on payments, medical, legal.
- Acknowledge every action; prefer undo over "Are you sure?"; toasts auto-dismiss in 3–5s, errors persist until resolved. Feedback closest to the action wins: inline, then component, then page, then system.
- Model stateful components as explicit state machines: states, events, transitions, guards, actions. Every state has a way out; no impossible states (loading and error together); each state maps to a UI representation. Design empty, loading, error, and success with the same care as the happy path. Empty states explain what belongs here and give one clear first action.

**Navigation, IA, search**
- Primary content ≤3 levels deep, findable in ≤3 clicks; labels from user vocabulary, validated with first-click tests (above 65% success is good). Mobile: 3–5 bottom tabs in thumb reach; labels required on Android. Never a hamburger for primary navigation on desktop. More than 7 top-level destinations means revisit the IA before adding items. Design navigation before individual screens.
- Active state distinguishable by more than colour. Critical items first or last in a list, never positions 3–5 of 7; the primary option never the middle of three.
- Search: placeholder names what is searchable, suggestions after 2–3 characters, 5–8 suggestions max, recent first, query persists after submit, applied filters visible and individually removable, zero results is a retention moment (confirm the query, suggest corrections, offer paths). Never remove search on mobile.
- Follow the conventions users already hold (Jakob's Law): logo top-left is home, X closes, magnifier is search, cart means checkout. Name a convention before departing from it; high-frequency interactions stay conventional. iOS vs Android: reserve the iOS left-edge swipe for back; no FAB on iOS; no iOS action sheets on Android or Android dialogs on iOS; up to 5 tabs on iOS, 3–5 with labels on Android.

**Localisation**
- Design for text expansion (German +20–35%, Finnish +30–40%; test navigation at 130% length); min-width not fixed width on buttons; logical CSS properties (`margin-inline-start`, `text-align: start`); directional icons mirror in RTL, logos, clocks, and numbers do not; 16px+ for Arabic and Hebrew; never fake-bold non-Latin scripts; locale-aware date, number, currency, and address formatting.

## Research and evidence discipline

- Before trusting a surprising number, rule out five things: the event does not mean what its name says; the denominator moved; the "step" is not an enforced step; a release, holiday, or campaign landed the same date; a platform split is hiding the effect. Then read the shape: a cliff means something blocks; a slope means the flow is too long and cutting one step moves little; retention that falls then flattens means a bad first run with a real core; retention that keeps falling means a value problem onboarding will not fix; a bimodal distribution means two populations, segment before designing.
- A hypothesis must forbid something. Rank hypotheses by how cheaply each can be killed, not by how likely they feel.
- Data answers where and how often; research answers why. Eight interviews cannot speak to a 40% rate. Weight revealed behaviour over stated preference. Never average two conflicting accounts into a compromise; write down what result would make you drop each, then run the one narrow study that discriminates. A completion gain and a comprehension loss are not on the same ledger.
- Interview and survey questions are non-leading and never yes/no ("How did you feel about that?" not "Was that frustrating?"). Surveys: one question per question, label scale endpoints, include a midpoint, keep under 5 minutes, about 385 responses for ±5% at 95% confidence, pilot with 3–5 people. SUS averages 68, above 80 is good. NPS: 9–10 promoters, 7–8 passives, 0–6 detractors.
- Synthesis indexes evenly across participants: tag every observation P1, P2, …; every participant appears in the output; single-source patterns are flagged, not dropped. 2–4 personas with one primary. Journeys in 5–7 stages with an emotional curve and 3–5 ranked opportunities. 5–8 participants per segment for usability tests; 20–50 for click tests; 8–15 for diary studies over 1–4 weeks; 3–5 independent evaluators for heuristic review with severity 0–4.

## Exploration and decision discipline

- When one direction is on the table, build a spread of concepts that differ in **what the user does** (sequence, unit of interaction, division of labour, entry point, commitment point), not how it looks. The same steps with different styling is one concept rendered twice. Hold fidelity and visual language constant across the set. Three cheap sketches beat two polished mockups. Never carry a concept you would refuse to build.
- Fix selection criteria **before** comparing; each must be able to fail a concept ("completes the core task in three steps or fewer", not "better UX"); mark each as threshold or trade-off. Evidence over volume. Name what the winner costs. A split set is a priority problem, not a design problem. Never graft losers onto the winner. For every rejected concept record what it tested, what it lost on, and what would bring it back.
- Prototype the riskiest assumption first; match fidelity to the question, not the deadline.

## Shipping and advocacy

- Handoff specs use token names, not raw values, and include every state, edge case (min and max content, text expansion, RTL), asset, keyboard behaviour, and implementation note. Verify with the QA checklist (visual, layout, interaction, content, accessibility, cross-platform) against the spec, not memory.
- Design the peak and the end of every flow deliberately: end on accomplishment, never on an administrative screen or an error. Autosave first; surface at most one or two open loops at a time.
- Defend design in the language of value: which line of the P&L does the decision move, what is the bet, what is the counterfactual, and which part is evidence versus craft judgment.

## What is in `references/`

- `workflows.md`: all 34 workflows with their ordered steps, the skill each step uses, and the output artifact.
- `<plugin>.md` (nine files): an index of every skill in that plugin with its full description, its "use when" trigger, and the path to its source, plus the plugin's workflows.
- `source/<plugin>/<skill>.md`: the unabridged source of each of the 111 skills, plus `*.evals.md` for the two that ship evals (`behavioural-analytics`, `qual-quant-triangulation`). This is the ground truth; read it before applying a skill.

To refresh the references after the upstream collection changes, run `python3 portable-skill/build.py` in the designer-skills repo and copy the folder again.
