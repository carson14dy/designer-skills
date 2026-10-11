# CLAUDE.md — working in designer-skills

This repo is the design-practice collection of the Designer Skills suite: 9 Claude Code plugins, 111 skills, 34 commands, each also compiled into a Gemini CLI extension under `.gemini/extensions/`. Skills are **nouns** (domain knowledge in `<plugin>/skills/<name>/SKILL.md`); commands are **verbs** (workflows in `<plugin>/commands/<verb>.md` that chain skills from the same plugin). `INDEX.md` arranges every skill by situation and lists the pairs most often confused.

When the user asks for an app, website, screen, flow, or any design artifact, this repo is the playbook. Treat the skills as the standard you are held to, not as optional reading.

## How to use the skills when designing for the user

1. **Route first.** Place the request on the grain **understand → frame → explore → make → validate → ship** (see `designer-toolkit/commands/start-here.md`). Starting one stage upstream is cheap; discovering a skipped stage after the build is not.
2. **Read the skills for that stage before producing anything.** Open the relevant `SKILL.md` files (use `INDEX.md` to find them) and apply them literally: every "Use when" clause, every table, every "do not". For a screen that means at minimum `layout-grid`, `visual-hierarchy`, `typography-scale`, `color-system`, `spacing-system`, `responsive-design`, `dark-mode-design`; for a flow add `state-machine`, `feedback-patterns`, `error-handling-ux`, `loading-states`; for a form, `form-design`, `hicks-law`, `millers-law`, `fitts-law`.
3. **Run the command's steps in order.** Commands are the pipelines: `/ui-design:design-screen`, `/interaction-design:design-form`, `/interaction-design:design-interaction`, `/interaction-design:design-onboarding`, `/prototyping-testing:explore-options`, `/visual-critique:critique-screen`, `/design-ops:handoff`. Name the skill driving each step in your output.
4. **Critique your own output before handing it over.** Run the seven visual-critique dimensions (hierarchy, brand, composition, typography, colour, affordance, density) on anything you build, in the format Observation / Problem / Fix, rated pass / minor issue / major issue, then prioritise P1 critical, P2 important, P3 polish.
5. **Write the rationale.** Decision, context, options considered, evidence, reasoning, trade-offs, validation plan (`design-rationale`). Write it during the decision, not after.

## Non-negotiables the skills encode (apply to every build)

**Accessibility and targets**
- Text contrast 4.5:1 minimum (AA), 3:1 for large text (18px+ regular, 14px+ bold) and for UI components against adjacent colours. Never convey meaning by colour alone; pair with icon, label, or pattern.
- Touch targets 44×44pt (Apple) / 48×48dp (Material); 24×24px minimum for pointer. Expand hit areas with padding, not visual size.
- Every field has a persistent, programmatic label. Placeholder text is never the only label. Errors are associated via `aria-describedby`, placed directly below the field, keyboard-focusable summary at top when multiple.
- Honour `prefers-reduced-motion` at the system level (replace slides/scales with instant or opacity; keep spinners/progress) and `prefers-color-scheme`, with a manual toggle too. Respect Dynamic Type / sp scaling; fixed text sizes are an accessibility failure.
- Visible, high-contrast focus state. Never `outline: none` without a replacement.

**Type, measure, spacing, layout**
- Body text 16px minimum; type scale on a ratio (1.25 or 1.333); 4–5 sizes in regular use; ≥1.25× between scale steps, ≥1.5× size difference between hierarchy levels. Line-height 1.2 headings / 1.5 body / 1.75 long-form. At most two weights active on one screen.
- Measure 45–75 characters (`max-width: 65ch`); 55–70 for long-form, 45–65 UI body, 40–60 captions, 30–45 pull quotes. Wider measure needs more leading.
- Spacing scale from a 4px or 8px base: 2, 4, 8, 16, 24, 32, 48, 64. Never arbitrary values. Within-group spacing tighter than between-group; label tighter to its input than to the next field; less space below a heading than above it.
- Grid: 4 / 8 / 12 columns (mobile / tablet / desktop); gutters 16–32px; margins 16px mobile, 24–48px desktop; breakpoints around 375 / 640 / 768 / 1024 / 1440. Test every breakpoint, not just the extremes.
- One primary CTA per view, filled; everything else ghost or text. If everything is emphasised, nothing is (Von Restorff). Decide the single most important element per screen in advance.
- Use the weakest container that works: spacing before background, background before border, border before card. Max two levels of nested containers. Remove borders iteratively and check whether the grouping still reads.
- Dark mode is not inversion: background ~#121212, elevation via lighter surfaces not shadows, desaturate primaries 10–20%, text off-white (#E0E0E0) not pure white, 4.5:1 still applies, provide dark illustration/logo variants, re-validate figure-ground and closure.

**Motion and latency**
- Durations: instant 50ms, fast 100ms, normal 200ms, moderate 300ms, slow 400ms, deliberate 600ms. Keep UI motion under 400ms; staggers 30–50ms; a staggered sequence under 500ms (700ms absolute ceiling). Ease-out (decelerate) entering, ease-in (accelerate) exiting, linear only for loops.
- Doherty: respond under 400ms. Button state change within 100ms. Autocomplete within 300ms. No loading indicator for anything under 100ms (flash of a spinner is itself disruptive); subtle indicator 100ms–1s; progress (not just a spinner) past 3s; time estimate and background option past 10s. Skeletons beat spinners when layout is known.
- Give 300–600ms recovery space after an error before the next prompt. Heavy news arrives slowly; good news can be instant.

**Forms, feedback, errors**
- Single column, top-aligned labels, field width reflects expected input length, mark optional not required, remove every optional field you can, default to the most common answer. Radios for ≤5 options, select for 6+, never freeform text for structured dates, show/hide on passwords.
- Validate on blur, not per keystroke. Error message says what happened and how to fix it, never blames the user, never "Something went wrong". Preserve input on error. Review step before submission on payments, medical, legal.
- Acknowledge every action; prefer undo over "Are you sure?"; toasts auto-dismiss 3–5s, errors persist until resolved. Feedback closest to the action wins (inline > component > page > system).
- Model stateful components as explicit state machines: every state has a way out; no impossible states (loading + error); map each state to a UI representation; design empty, loading, error, and success with the same care as the happy path.

**Navigation, IA, search**
- Primary content ≤3 levels deep; findable in ≤3 clicks; labels from user vocabulary, validated with first-click tests (above 65% first-click success is good). Mobile: 3–5 bottom tabs in thumb reach, labels required on Android. Never hamburger for primary nav on desktop. More than 7 top-level destinations means revisit the IA.
- Active nav state distinguishable by more than colour. Critical items first or last in a list, never positions 3–5 of 7 (serial position valley); primary CTA never the middle of three.
- Search: placeholder names what is searchable, suggestions after 2–3 characters, 5–8 suggestions max, recent first, query persists in the field, zero results is a retention moment (confirm query, suggest corrections, offer paths), never remove search on mobile.
- Follow the conventions users already hold (Jakob's Law): logo top-left is home, X closes, magnifier is search. Name a convention before departing from it; high-frequency interactions stay conventional. iOS vs Android: reserve iOS left-edge swipe for back; no FAB on iOS; no iOS action sheets on Android or Android dialogs on iOS.

**Localization**
- Design for +30–40% text expansion (German/Finnish as worst case); min-width not fixed width on buttons; logical CSS properties (`margin-inline-start`, `text-align: start`); directional icons mirror in RTL, logos/clocks/numbers do not; 16px+ for Arabic/Hebrew; never fake-bold non-Latin scripts; locale-aware date/number/address formatting.

## Research and evidence discipline

- Before trusting a surprising number, rule out: the event does not mean what its name says; the denominator moved; the "step" is not an enforced step; a release/holiday/campaign landed the same date; a platform split is hiding the effect. Read the shape (cliff = block; slope = too long; retention falls-then-flattens = bad first run but real core; keeps falling = value problem; bimodal = two populations, segment first).
- A hypothesis must forbid something; rank by how cheaply it can be killed.
- Data answers where / how often; research answers why. Eight interviews cannot speak to a 40% rate. Weight revealed behaviour over stated preference. Never average two conflicting accounts into a compromise; design the narrow study that would change your mind.
- Interview and survey questions are non-leading and never yes/no ("How did you feel about that?" not "Was that frustrating?"). Surveys: one question per question, label scale endpoints, keep under 5 minutes, ~385 responses for ±5% at 95%, pilot with 3–5 people. SUS: 68 average, 80+ good. NPS: 9–10 promoters, 7–8 passives, 0–6 detractors.
- Synthesis indexes evenly across participants: tag every observation P1, P2…; every participant appears in the output; single-source patterns are flagged, not dropped. 2–4 personas, one primary. Journeys 5–7 stages. 5–8 participants per segment for usability tests; 20–50 for click tests; 3–5 evaluators for heuristic review (severity 0–4).

## Exploration and decision discipline

- When one direction is on the table, build a spread of concepts that differ in **what the user does** (sequence, unit of interaction, division of labour, entry point, commitment point), not how it looks. Same steps with different styling is one concept rendered twice. Hold fidelity constant across the set. Three cheap sketches beat two polished mockups.
- Fix selection criteria **before** comparing; each must be capable of failing a concept; mark threshold vs trade-off. Evidence over volume. Name what the winner costs. Never graft losers onto the winner. Record for every rejected concept what it tested, what it lost on, and what would bring it back.
- Prototype the riskiest assumption first; match fidelity to the question, not the deadline.

## Handoff and shipping

- Specs use token names, not raw values; include every state, edge case (min/max content, text expansion, RTL), asset, and keyboard behaviour. Verify with the QA checklist (visual, layout, interaction, content, accessibility, cross-platform) against the spec, not memory.
- Design the peak and the end of every flow deliberately (Peak-End): end on accomplishment, never on an administrative screen or an error.

## Editing this repo

- Follow `CONTRIBUTING.md`. Skill `name` matches its directory, kebab-case; description under 400 chars with a "Use when …" sentence and a boundary clause against the nearest neighbour; cross-plugin skill references are written `` `skill` (plugin) ``; commands need `description` and a quoted bracketed `argument-hint`, 3–7 steps each naming a same-plugin skill; no cross-plugin skill references in commands.
- Quote any frontmatter value containing brackets, a colon, or bare yes/no (YAML coercion silently broke four skills on Copilot CLI, issue #27).
- Before committing, run and commit the output of all six checks; CI fails on any drift:
  ```
  python3 scripts/lint-frontmatter.py
  python3 scripts/check-runtimes.py
  python3 scripts/generate-readmes.py
  python3 scripts/generate-index.py
  bash   scripts/build-gemini.sh
  python3 scripts/check-marketplace.py
  ```
- `INDEX.md` tables, plugin READMEs, the root README counts/commands table, and `.gemini/extensions/*/GEMINI.md` are generated; edit the source `SKILL.md` or command, then regenerate. The "Start here" and "Frequently confused" sections of `INDEX.md` are hand-written and linted for dead pointers.
- New skills or commands require an open issue first; one focused change per PR.
