# designer-toolkit

Advocate: rationale, negotiation, decks, case studies, copy, adoption.

Essential designer utilities for writing rationale, building presentations, crafting case studies, UX writing, and driving adoption.

Each row is one skill. The description is what the skill produces, when to use it, and the boundary against its nearest neighbour; the trigger column is the clause to match against the situation in front of you. Read the source file before applying the skill: it holds the rules, numbers, tables, and the "do not" lines that the description only points at.

| Skill | Reach for it | Description | Source |
| --- | --- | --- | --- |
| `case-study` | Use when telling a project's story to an external audience | Craft a portfolio case study with narrative arc, process evidence, and outcomes. Use when telling a project's story to an external audience. For an internal stakeholder deck, use `presentation-deck`. | `source/designer-toolkit/case-study.md` |
| `design-negotiation` | Use in the conversation itself | Advocate for design quality, scope, and timeline with partners and leadership using evidence and shared goals. Use in the conversation itself. For the commercial vocabulary behind it, use `business-design` (ux-strategy). | `source/designer-toolkit/design-negotiation.md` |
| `design-rationale` | Use when a decision needs defending in writing | Write rationale connecting decisions to user needs, business goals, and principles. Use when a decision needs defending in writing. For a live conversation, use `design-negotiation`. | `source/designer-toolkit/design-rationale.md` |
| `design-system-adoption` | Use when the system exists but teams ignore it | Create adoption strategy and enablement materials to drive design system usage. Use when the system exists but teams ignore it. For contribution and versioning rules, use `design-system-governance` (design-systems). | `source/designer-toolkit/design-system-adoption.md` |
| `design-token-audit` | Use when tokens exist and you suspect they are being bypassed | Audit token usage across a product for coverage, drift, and hard-coded values. Use when tokens exist and you suspect they are being bypassed. For defining tokens in the first place, use `design-token` (design-systems). | `source/designer-toolkit/design-token-audit.md` |
| `presentation-deck` | Use when presenting internally | Structure a design presentation for a specific audience and decision. Use when presenting internally. For a portfolio narrative use `case-study`; for the written argument use `design-rationale`. | `source/designer-toolkit/presentation-deck.md` |
| `ux-writing` | Use when the words are the deliverable | Write interface copy — microcopy, error messages, empty states, and CTAs. Use when the words are the deliverable. For content structure and ownership, use `content-strategy` (ux-strategy). | `source/designer-toolkit/ux-writing.md` |

## Workflows in designer-toolkit

Full steps in `workflows.md`.

- `/designer-toolkit:build-presentation`: Build a design presentation end to end — audience framing, narrative structure, and supporting rationale.
- `/designer-toolkit:start-here`: Find where to start in the collection — name what you're working on and get routed to one command, the two that follow it, and the stages you can skip.
- `/designer-toolkit:write-case-study`: Build a portfolio case study end to end — project framing, process narrative, outcomes, and visuals.
- `/designer-toolkit:write-rationale`: Write design rationale for a set of decisions, linking each to user needs, business goals, and principles.
