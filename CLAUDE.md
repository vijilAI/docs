# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

## Development Commands

```bash
mint dev              # local preview at http://localhost:3000
mint broken-links     # check internal links before opening a PR
vale <file.mdx>       # lint prose (run `vale sync` once to fetch packages)
vale .                # lint everything
python3 -c "import json; json.load(open('docs.json'))"   # validate docs.json after edits
```

## Repository Overview

Source for [docs.vijil.ai](https://docs.vijil.ai), built with [Mintlify](https://mintlify.com). Content is MDX. Navigation is driven entirely by `docs.json`: a page that is not registered there does not appear on the site. Mintlify publishes `main` to the live site.

### Navigation Tabs (`docs.json`)

- **Concepts** (`concepts/`): mental models. Platform overview (Console, Discover, Diamond, Dome, Darwin), Trust Score and its three dimensions, Discovery components (Target, Collector, Resource, Classification), Evaluation components (Harness, Scenario, Probe, Detector), Red Team (Engagements), Runtime Defense (Guardrail, Guard, Detector, Observe), Glossary.
- **Agent Owner's Guide** (`owner-guide/`): Console workflows for non-developers. Teams, Discover, Agents, evaluation environment (Personas, Policies, Harnesses), evaluations, Red Team, Protect (Guardrails, Defend, deploying Dome, observability).
- **Agent Developer's Guide** (`developer-guide/`): programmatic integration. Quickstart, Claude Code plugin, self-hosted Console, evaluations (SDK/MCP/REST), Red Team, Dome (`vijil-dome`: install, Control Engine, Trust Runtime, Guardrails, Detectors, framework integrations), Reference (MCP tools, Controls API, SDK Reference, API Reference).

Only one page under `tutorials/` is in the nav (`tutorials/protect-agents/dome-containerized-deployment`). The other `tutorials/*` files and the top-level `core-concepts/`, `evaluate-agents/`, `manage-agents/`, `protect-agents/`, and `references/python-client/` directories are orphans (not in `docs.json`). Do not link to them or copy facts from them without re-verifying; they are pending a register-or-delete pass.

### Products

- **Console**: the web app. Sidebar actions are **Discover**, **Verify** (evaluations), **Defend** (runtime events), **Evolve** (Darwin); registries are Agents, Personas, Policies, Harnesses.
- **Discover**: finds AI agents and systems in your estate (Targets, Collectors, Resources) so you can register the ones worth governing.
- **Diamond**: evaluation. Runs Harnesses of Probes and returns a Trust Score across reliability, security, and safety.
- **Red Team**: adaptive, multi-turn adversarial Engagements (the "Adaptive" evaluation type in the Console).
- **Dome** (`vijil-dome` on PyPI): runtime protection. Content Guards (Guardrail → Guard → Detector), the Trust Runtime (`secure_agent()`), and the Control Engine. Can report telemetry to the Console and enforce Console-managed config.
- **Darwin**: evolves agents from evaluation and production feedback (Console **Evolve**).

### Interfaces and Audience

- The **Vijil CLI is internal. Never document it**: no `vijil <command>` snippets, no CLI tabs, no `vijil auth login` or `vijil config set`. Third-party CLIs (gcloud, AWS, kubectl) and the `vijil-dome[trust-cli]` extra name are fine.
- Public interfaces: **Console (UI)**, **MCP** (`vijil-mcp`, configured with env vars in `.mcp.json`), the **Python SDK** (`vijil-sdk`, `from vijil import Vijil`), and the **REST API**.
- **Owner's Guide pages show only Console and MCP.** SDK and REST content belongs in the Developer's Guide, which links back to the Owner's Guide for "what it does" content.
- Task pages use `<Tabs>`, one per interface, in the order Console → MCP → SDK → REST API. Reference pages stay whole, not tabbed.
- SDK auth: `VIJIL_CLIENT_ID` + `VIJIL_CLIENT_SECRET` is primary, `VIJIL_API_KEY` is the alternative. SDK config lives in `~/.vijil/config.toml` (document file edits, not CLI commands).

### Sources of Truth

The docs follow the product repos, not the other way round. Verify behavior in source before writing it:

| Topic | Repo (GitHub `vijilAI/…`) |
| --- | --- |
| Console backend, API, MCP tools, Red Team | `vijil-console` (local checkout at `~/Projects/vijil/console` is often stale; use `git archive origin/main` or `gh`) |
| Console UI labels, sidebar, tabs | `vijil-console-frontend` (no local checkout; `gh repo clone … -- --depth 1`) |
| Dome, Trust Runtime, extras | `vijil-dome` (check `pyproject.toml` for extras) |
| Python SDK | `vijil-sdk` |
| Detectors and evaluation engine | `vijil-diamond` |
| Discover Collectors | `vijil-shadow`, `vijil-endpoint-agent` |
| Red Team engine | `vijil-redteam` |

Do not copy internal hostnames (`dev05`, `saas`), AWS account IDs, or internal runbook URLs into the docs.

## Writing Style

Vale runs `VijilStyle`, `Vale`, `write-good`, and `proselint` on every `.mdx` file (`.vale.ini`, custom rules in `.styles/VijilStyle/`).

Enforced by Vale:

- **Capitalize component names**: Harness, Scenario, Probe, Detector, Guard, Guardrail (singular and plural). Lowercase is an error.
- **No contractions**: "do not", not "don't".
- **Headings**: H2 (`##`) and H3 (`###`) only, in Title Case.
- **Second person**: "you", not "we/our/us".
- **Inline code**: backticks for filenames, flags, env vars, and function calls.

House rules (not all caught by Vale):

- **No em dashes** in prose. Use commas, parentheses, or two sentences. Avoid en dashes in ranges ("2 to 5"). Grep changed files for `—` before finishing.
- **Overview, not deep dive.** Explain what a feature does and what the reader sees or does. Skip internals, and do not write per-tab, per-column, or per-field tables; the UI changes every release. When turning release notes into docs, keep only what changes what the reader does or sees.
- **Prefer Mintlify components**: `<Steps>`, `<Tabs>`, `<CardGroup cols={N}>`, `<AccordionGroup>`, and callouts (`<Note>`, `<Tip>`, `<Warning>`, `<Info>`, `<Check>`).
- **Icons are lucide**, not Font Awesome (`shield`, `bot`, `workflow`, `server`). Font Awesome-only names render blank.
- **No markdown bullet lists inside `<Card>`**; the card CSS doubles them. Use short paragraphs with bold lead-ins.
- Use bare code fences rather than `<CodeGroup>`, which makes Vale lint the code.
- **Diagrams**: use Mermaid, not images. No screenshots in Discover pages.
- "Vijil" trips `Vale.Spelling`; that is known and tolerated.

## Adding or Changing Pages

1. Create the `.mdx` file with frontmatter:
   ```mdx
   ---
   title: 'Page Title'
   description: 'One-line description that reads naturally.'
   ---
   ```
2. Register it in the right `navigation.tabs[].groups[].pages` array in `docs.json`. When you move or delete a page, add a `redirects` entry.
3. Run `vale` on the changed files and `mint broken-links`.
4. Drafts go in `drafts/` or use `.draft.mdx`; `.mintignore` excludes both.

Do not hand-edit `openapi/api.json`. `.github/workflows/sync-api-spec.yml` regenerates it from the Console's `specs/` with `scripts/merge_openapi.py`.

## Agent Skill (`skill.md`)

`skill.md` at the repo root is the agent skill Mintlify serves at `https://docs.vijil.ai/skill.md` and `/.well-known/skills/`. It overrides Mintlify's auto-generated skill. `.agents/skills/vijil/SKILL.md` is a locally installed copy (`npx skills add docs.vijil.ai`, tracked in `skills-lock.json`) and should match `skill.md`.

Update `skill.md` whenever a change affects how an agent uses Vijil: package names, auth, SDK methods, MCP tools, REST endpoints, Harness names, Trust Score scale, or Dome config. It follows the same rules as the docs (no CLI, no em dashes).

## Workflow

- Docs work is tracked in [GitHub Issues](https://github.com/vijilAI/docs/issues). Product releases open `[Docs Update] <repo> <tag> released` issues (label `docs-update`) through `.github/workflows/docs-release-notify.yml`. Close one by updating the affected pages or noting that no change is needed.
- Branch from `main` with `git switch -c docs/<topic> --no-track origin/main` (never a branch that tracks `origin/main`; a plain `git push` once landed on `main`). Use `ci/<topic>` for automation.
- Use Conventional Commits: `docs: Add Discover overview`. PRs are squash-merged.
- **Do not commit, push, or open PRs yourself.** Finish each change with a short, copyable commit message in chat.
- Do not render pages or take screenshots to verify visuals. Run `vale` and `mint broken-links`; the user checks the result in `mint dev`.

### Literally Portal Task

The docs are delivered through Literally Portal (`literally-portal` MCP server, Vijil board **Tasks**, `board_id` `d2a934bb-0e68-4883-96b6-a0a1217fb723`). For every new docs task:

1. **At the start**, before editing, ask the user whether to create a Portal task. Propose a title, a short description of the work, and an assignee. Do not create it without a yes.
2. On a yes, call `create_task` with the title and description. It takes no assignee, so then call `get_task` to read person refs (or `list_mentionable_people` with `target: "task"`) and set the assignee with `update_task`.
3. **When the PR exists**, ask the user for the PR URL and add it to the task description with `update_task`.
