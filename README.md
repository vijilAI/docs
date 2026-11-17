# Vijil Documentation

Source for [docs.vijil.ai](https://docs.vijil.ai), built with [Mintlify](https://mintlify.com).

## Setup

Requirements: Node.js 20+ and [Vale](https://vale.sh/docs/install).

```bash
npm i -g mint   # Mintlify CLI
vale sync       # download the write-good and proselint packages
mint dev        # preview at http://localhost:3000
```

## Repository Layout

| Path | Contents |
| --- | --- |
| `concepts/` | Mental models: Trust Score, evaluation and defense components |
| `owner-guide/` | Agent Owner's Guide: Console and MCP workflows |
| `developer-guide/` | Agent Developer Guide: SDK, API, CI/CD, frameworks, self-hosted deployment |
| `tutorials/` | Walkthroughs linked from both guides |
| `references/` | Glossary and reference tables |
| `openapi/api.json` | API reference spec, synced from the Console (do not edit by hand) |
| `.styles/VijilStyle/` | Custom Vale rules |
| `scripts/` | Maintenance scripts (OpenAPI merge, image cleanup) |

Drafts go in `drafts/` or use the `.draft.mdx` extension. Mintlify skips both.

## Writing a Page

1. Create the `.mdx` file with a `title` and a `description` in the frontmatter.
2. Register its path in `docs.json`. A page that is not listed there does not appear in the site navigation.
3. Run Vale on the file and fix the errors:

   ```bash
   vale path/to/page.mdx
   ```

4. Check links before you open a PR:

   ```bash
   mint broken-links
   ```

The main style rules, enforced by Vale:

- Capitalize component names: Harness, Scenario, Probe, Detector, Guard, Guardrail.
- No contractions, no em dashes.
- Use only H2 and H3 headings, in Title Case.
- Write in the second person ("you").
- Put file names, flags, and code in backticks.
- Prefer Mintlify components (`<Steps>`, `<CardGroup>`, `<Tabs>`, callouts) over long prose or tables.
- Keep product pages at overview level. Explain internals only when the reader needs them to act.

## Workflow

1. Branch from `main` with a prefix: `docs/<topic>` for content, `ci/<topic>` for automation.
2. Use [Conventional Commits](https://www.conventionalcommits.org) style: `docs: Add Discover overview`, `ci: Pin checkout action`.
3. Open a PR into `main`. PRs are squash-merged, and Mintlify publishes `main` to the live site.

## Issues and Automation

Track all docs work in [GitHub Issues](https://github.com/vijilAI/docs/issues).

| Source | What happens |
| --- | --- |
| Product release | Each Vijil product repo calls `.github/workflows/docs-release-notify.yml` when it cuts a release. The workflow opens a `[Docs Update] <repo> <tag> released` issue labeled `docs-update`, with a review checklist. It includes release notes only for public repos. |
| API changes | `.github/workflows/sync-api-spec.yml` runs on weekdays at 13:00 UTC. It merges the Console's service specs into `openapi/api.json` and opens or updates a PR labeled `api-spec`. Before merging, check that new endpoints should be public and that removed ones are not still linked. |
| Anything else | Open an issue with a `type:` label (`type: doc` or `type: bug`) and a priority (`P0` to `P2`). |

To close a `docs-update` issue, review the release notes, then either update the affected pages or note on the issue that the release needs no change.
