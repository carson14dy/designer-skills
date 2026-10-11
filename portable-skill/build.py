#!/usr/bin/env python3
"""Rebuild the portable design-playbook skill's references/ from this repo.

Run after any skill or command changes upstream:
    python3 portable-skill/build.py

What it regenerates (SKILL.md is hand-written and left alone):
  references/workflows.md        every command as a workflow, with steps and output
  references/<plugin>.md         per-plugin index: each skill's description, use-when
                                 trigger, boundary, and the path to its full source
  references/source/<plugin>/    unabridged copy of every SKILL.md (renamed to
                                 <skill>.md so no runtime discovers them as skills)
                                 plus any EVALS.md as <skill>.evals.md
"""
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "portable-skill" / "design-playbook"
REFS = SKILL / "references"
PLUGINS = ["design-research", "ux-strategy", "ui-design", "interaction-design",
           "design-systems", "prototyping-testing", "visual-critique", "design-ops",
           "designer-toolkit"]
STAGE = {
    "design-research": "Understand: users, context, and the problem as it actually is.",
    "ux-strategy": "Frame: the problem, the direction, and what matters.",
    "ui-design": "Make (surface): layout, type, colour, spacing, perception.",
    "interaction-design": "Make (behaviour): flows, forms, feedback, motion, cognitive laws.",
    "design-systems": "Systematise: tokens, components, and the rules that keep them coherent.",
    "prototyping-testing": "Explore and validate: concepts, prototypes, tests, experiments.",
    "visual-critique": "Validate by eye: the seven screen critiques.",
    "design-ops": "Ship: handoff, QA, review, sprints, debt, impact.",
    "designer-toolkit": "Advocate: rationale, negotiation, decks, case studies, copy, adoption.",
}
TRIGGER = re.compile(r"(?:^|\.\s)(Use\s+.*?)(?:\.\s|\.$|$)")


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    fm = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip().strip('"')
    return fm, m.group(2)


def plugin_blurb(plugin):
    readme = (ROOT / plugin / "README.md").read_text(encoding="utf-8").splitlines()
    seen_h1 = False
    for line in readme:
        if line.startswith("# "):
            seen_h1 = True
            continue
        if seen_h1 and line.strip():
            return line.strip()
    return ""


def build_sources():
    if (REFS / "source").exists():
        shutil.rmtree(REFS / "source")
    n = 0
    for p in PLUGINS:
        out = REFS / "source" / p
        out.mkdir(parents=True)
        for d in sorted((ROOT / p / "skills").iterdir()):
            shutil.copy(d / "SKILL.md", out / f"{d.name}.md")
            n += 1
            if (d / "EVALS.md").exists():
                shutil.copy(d / "EVALS.md", out / f"{d.name}.evals.md")
    return n


def build_plugin_index(p):
    lines = [f"# {p}", "", STAGE[p], "", plugin_blurb(p), "",
             "Each row is one skill. The description is what the skill produces, when to use "
             "it, and the boundary against its nearest neighbour; the trigger column is the "
             "clause to match against the situation in front of you. Read the source file "
             "before applying the skill: it holds the rules, numbers, tables, and the \"do not\" "
             "lines that the description only points at.", "",
             "| Skill | Reach for it | Description | Source |", "| --- | --- | --- | --- |"]
    for d in sorted((ROOT / p / "skills").iterdir()):
        fm, _ = frontmatter(d / "SKILL.md")
        desc = fm["description"]
        m = TRIGGER.search(desc)
        trig = (m.group(1).rstrip(".") if m else "")
        src = f"`source/{p}/{d.name}.md`"
        if (d / "EVALS.md").exists():
            src += f" + `source/{p}/{d.name}.evals.md`"
        lines.append(f"| `{d.name}` | {trig} | {desc.replace('|', '/')} | {src} |")
    cmds = sorted((ROOT / p / "commands").glob("*.md"))
    lines += ["", f"## Workflows in {p}", "",
              "Full steps in `workflows.md`.", ""]
    for c in cmds:
        fm, _ = frontmatter(c)
        lines.append(f"- `/{p}:{c.stem}`: {fm['description']}")
    (REFS / f"{p}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_workflows():
    lines = ["# Workflows (the 34 commands of the designer-skills collection)", "",
             "Each workflow chains skills from one plugin into a complete job. In the source "
             "collection these are slash commands (`/plugin:verb`); inside this playbook you run "
             "them yourself: follow the steps in order, apply the named skill at each step (find "
             "it in `references/<plugin>.md`, read it in `references/source/<plugin>/<skill>.md`), "
             "and produce the stated output. A step that says \"suggest `/x`\" means: name that "
             "workflow as the natural next step.", ""]
    for p in PLUGINS:
        lines += [f"## {p}", ""]
        for cmd in sorted((ROOT / p / "commands").glob("*.md")):
            fm, body = frontmatter(cmd)
            body = re.sub(r"^# /[\w-]+\n", "", body.strip() + "\n", count=1)
            body = re.sub(r"(?m)^## ", "#### ", body)
            lines += [f"### /{p}:{cmd.stem}", "", f"**{fm['description']}**", "",
                      f"Input: {fm['argument-hint']}", "", body.strip(), ""]
    (REFS / "workflows.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    REFS.mkdir(parents=True, exist_ok=True)
    n = build_sources()
    for p in PLUGINS:
        build_plugin_index(p)
    build_workflows()
    print(f"design-playbook: {n} skills copied, {len(PLUGINS)} plugin indexes, workflows.md rebuilt")
