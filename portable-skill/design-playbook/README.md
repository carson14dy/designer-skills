# design-playbook

The design-practice collection of the Designer Skills suite (9 plugins, 111 skills, 34 workflows) packaged as a single Claude Code skill, for projects that are not this repo and do not have the plugins installed.

## Install in another project

Copy this folder into the project's skills directory and commit it:

```
mkdir -p <your-project>/.claude/skills
cp -r portable-skill/design-playbook <your-project>/.claude/skills/
```

Claude Code picks it up on the next session. It fires on its own whenever the work is design (a screen, a flow, a form, a critique, a research plan), and you can also call it directly with `/design-playbook`. To make it available in every project on your machine instead, copy it to `~/.claude/skills/design-playbook/`.

## What is inside

- `SKILL.md`: the router. How to place a request on the understand → frame → explore → make → validate → ship grain, which skills to read at each stage, the routing map from `/start-here`, the pairs most often confused, and every hard number and anti-pattern the 111 skills agree on.
- `references/workflows.md`: all 34 workflows with ordered steps, the skill each step uses, and the output.
- `references/<plugin>.md`: one index per plugin, listing each skill's description, trigger, and source path.
- `references/source/<plugin>/<skill>.md`: the full text of every skill, unchanged apart from the filename.

## Keeping it current

`references/` is generated. After pulling upstream changes into designer-skills, run:

```
python3 portable-skill/build.py
```

then copy the folder into your project again. `SKILL.md` is hand-written and is not touched by the build.

## Attribution

Skills and workflows by MC Dean, from [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills), MIT licensed. This packaging keeps that license.
