# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

```bash
# Start the local dev server (preview at localhost:3000)
mint dev

# Lint prose with Vale
vale <file.mdx>
vale .   # lint all files
```

## Repository Overview

This is the Vijil documentation site built with [Mintlify](https://mintlify.com). Content is written in MDX (Markdown + JSX). The site structure and navigation are entirely driven by `docs.json` — adding a new page requires registering it there.

### Content Structure

The docs are organized into four top-level tabs defined in `docs.json`:

- **Concepts** (`concepts/`) — Mental models: Trust Score (reliability/security/safety), evaluation components (Harness → Scenario → Probe → Detector), and runtime defense components (Guardrail → Guard → Detector).
- **Agent Owner's Guide** (`owner-guide/`) — Console-based workflows for non-developers: register agents, build evaluation environments, run evaluations, configure Dome.
- **Agent Developer Guide** (`developer-guide/`) — Programmatic integration: SDKs, CLI, APIs, CI/CD, frameworks.
- **Legacy Docs** (`legacy/`) — Older content preserved for reference. Prefer the non-legacy equivalents for new content.

Tutorials live in `tutorials/` and are cross-referenced from both the Owner's Guide and Developer Guide tabs.

### Key Products

- **Diamond** — Evaluation product. Sends adversarial Probes, returns a Trust Score (0–1) across reliability, security, and safety.
- **Dome** — Runtime protection product. Intercepts inputs/outputs through Guardrails built from Guards and Detectors.

## Writing Style Rules (enforced by Vale)

Vale runs the `VijilStyle`, `write-good`, and `proselint` rulesets against all `.mdx` files. Key rules:

- **Capitalize component names**: Harness, Scenario, Probe, Detector, Guard, Guardrail (both singular and plural). Lowercase versions are Vale errors.
- **No contractions**: Write "do not" not "don't", "cannot" not "can't", etc.
- **Headings**: Use only H2 (`##`) and H3 (`###`). H1 and H4+ are errors.
- **Heading case**: Headings must be in Title Case.
- **Second person**: Prefer "you" over "we/our/us" unless "we" is explicitly defined.
- **Inline code**: Wrap filenames, CLI flags, and function calls in backticks.

Vale config is in `.vale.ini`; custom rules are in `.styles/VijilStyle/`.

## Adding Pages

1. Create the `.mdx` file with frontmatter:
   ```mdx
   ---
   title: 'Page Title'
   description: 'One-line description.'
   ---
   ```
2. Register the page path in the appropriate `navigation.tabs[].groups[].pages` array in `docs.json`.
3. Draft files go in `drafts/` or use the `.draft.mdx` extension — these are excluded from the build via `.mintignore`.

