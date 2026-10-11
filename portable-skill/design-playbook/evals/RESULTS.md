# design-playbook: test results

Three realistic prompts (`evals.json`), each run through `claude -p` in a clean, empty project folder, once with the skill installed at `.claude/skills/design-playbook/` from the packaged `.skill` and once without. Ten objective checks per prompt, graded by independent grader agents following the skill-creator grader protocol, with contrast ratios and structural checks verified by script. The skill triggered from its description in every with-skill run; the prompts never named it.

| Prompt | No skill | Skill v1 | Skill v2 | Skill v2.1 |
| --- | --- | --- | --- | --- |
| Photographer SaaS signup and first-run spec | 9/10 | 10/10 | 10/10 | not re-run |
| Ops dashboard critique | 6/10 | 10/10 | 10/10 | not re-run |
| Teal colour and type token system | 9/10 | 7/10 | 7/10 | layering fixed (see below) |
| Total | 24/30 (80%) | 27/30 (90%) | 27/30 (90%) | |

## What each version changed

- **v1** (first package): triggered reliably, but the runs opened 0 to 3 source skills before answering. The critique run read only the plugin index. Outputs claimed skills they had not opened.
- **v2**: added the per-task reading list. Runs opened 6 to 14 sources (all seven critique files for the critique). Format and traceability improved (per-dimension ratings, fix-order lists, seven-heading rationale); the pass count did not move because the checks do not measure those things.
- **v2.1**: added the three-tier token rule with an example, the neutral-scale requirement, and made the closing self-critique and rationale explicit deliverable sections. On the teal prompt, alias-tier tokens went from 0 of 126 referencing the raw scale to 205 of 219 (the rest are chart palette literals), a 14-step neutral scale appeared, and the deliverable closed with all seven dimensions, P1 to P3 fixes, and a rationale with trade-offs. Not formally re-graded; checked by script.

## Where the skill clearly helps

Critique and review work. The dashboard critique went from a flat list with two conflicting orderings to named dimensions with ratings, explicit P1/P2/P3 tiers in fix order, the 14px/16px type floors, and the logo-top-left convention. Specs gained complete state coverage (every screen with empty, loading, error, success) and a 100ms indicator rule.

## Where it does not yet help, or costs

- The teal token prompt: the baseline already does well, and v1/v2 shipped a raw scale nobody referenced. v2.1 addresses this; it should be re-graded alongside the other two prompts in the next iteration.
- Cost: with the skill, total tokens processed per run (including cache reads across turns) were 2 to 4 times the baseline; wall time rose 6 to 116 seconds.
- Small factual slips appeared in with-skill outputs (one misattributed contrast ratio, one broken cross-reference, a self-critique naming sizes not in the spec). Nothing in the checks catches these yet.

## Eval set feedback from the graders

19 of 30 checks pass with and without the skill, so the delta understates the visible differences. Next revision: add checks for the per-dimension rating, fix-order list, closing rationale, "no error copy says Something went wrong", loading indicator only after 100ms, and cross-reference integrity; split the bundled type-scale check; make the contrast check cover every text-on-fill token, not only pairs the run lists.

Workspace with transcripts, outputs, and grading for every run lives outside the repo (session scratchpad); regenerate by re-running the prompts in `evals.json` the same way.
