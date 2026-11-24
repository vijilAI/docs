---
name: vijil
description: Use when evaluating AI agents for trustworthiness (reliability, security, safety) before deployment, red teaming agents with adaptive adversarial attacks, protecting agents at runtime with Vijil Dome Guardrails, Controls, or the Trust Runtime, discovering AI agents in an estate, or gating CI/CD on a Vijil Trust Score. Covers the Vijil Python SDK (vijil-sdk), the vijil-mcp server and Claude Code plugin, the REST API, and the vijil-dome package.
metadata:
  mintlify-proj: vijil
  version: "2.0"
---

# Vijil

## Product Summary

Vijil is a trust platform for AI agents. It discovers agents in your estate, measures how trustworthy they are, protects them at runtime, and improves them from feedback.

| Product | What it does | Console sidebar |
|---------|--------------|-----------------|
| **Discover** | Finds AI agents, models, and services (Targets, Collectors, Resources) so you can register the ones worth governing | Discover |
| **Diamond** | Runs evaluations. A `behavioral` evaluation runs Harnesses of Probes and returns a Trust Score. A `redteam` evaluation runs an adaptive, multi-wave Engagement (no Trust Score) | Verify |
| **Dome** (`vijil-dome`) | Runtime protection: Content Guardrails (Guardrail > Guard > Detector), the Controls Engine (policy as data), and the Trust Runtime (identity, tool permissions, attestation, audit) | Defend |
| **Darwin** | Proposes agent improvements from evaluation and production feedback | Evolve |

Docs: https://docs.vijil.ai (full page index: https://docs.vijil.ai/llms.txt).

## Interfaces

Use these four interfaces. Vijil does not ship a public CLI; do not run or suggest `vijil <command>` shell commands.

| Interface | Install | Use it for |
|-----------|---------|------------|
| Console | https://console.vijil.ai | Interactive work, approving Policy rules and Darwin proposals |
| MCP server | `pip install vijil-mcp` (Python 3.10+) | Natural-language operation from Claude Code and other MCP clients |
| Claude Code plugin | `/plugin marketplace add vijilAI/vijil`, then `/plugin install vijil@vijil` (needs `uv`) | `/vijil inspect`, `evaluate`, `analyze`, `protect`, `adapt`, `register` |
| Python SDK | `pip install vijil-sdk` (Python 3.12+), `from vijil import Vijil` | Scripts, notebooks, CI/CD gates |
| REST API | Base URL `https://console-api.vijil.ai/v1`, header `Authorization: Bearer <token>` | Any other language |
| Dome | `pip install vijil-dome[...]`, `from vijil_dome import Dome` | Guardrails inside your agent process |

## Authentication

Create an API key in the Console under **Settings > API Keys**. You get a client ID (`vk_...`) and a secret that is shown once.

```bash
export VIJIL_CLIENT_ID="vk_..."          # preferred: exchanged for a short-lived token and renewed automatically
export VIJIL_CLIENT_SECRET="..."
export VIJIL_TEAM_ID="<team-id>"          # always set in CI; a token can belong to several teams
# export VIJIL_API_KEY="<bearer-token>"   # alternative: raw bearer token, not refreshable
# export VIJIL_CONSOLE_URL="https://console-api.<your-domain>"   # self-hosted Console (MCP, plugin, Dome)
```

- **SDK** credential order: `client_id`/`client_secret` arguments, `api_key` argument, `VIJIL_CLIENT_ID`/`VIJIL_CLIENT_SECRET`, `VIJIL_API_KEY`, then `~/.vijil/credentials.json`. Missing credentials raise `VijilAuthError`.
- **SDK gateway**: `Vijil(gateway=...)`, then `[gateway] url` in `~/.vijil/config.toml`, then `https://console-api.vijil.ai`.
- **SDK team**: `team_id=` argument, then `VIJIL_TEAM_ID`, then `[defaults] team_id` in `~/.vijil/config.toml`, then the first team in the token. Check `client.team_id`.
- **MCP**: pass the same env vars in the server's `env` block. Add `VIJIL_CA_BUNDLE` for a self-hosted Console behind a private CA.

```json
{
  "mcpServers": {
    "vijil": {
      "type": "stdio",
      "command": "vijil-mcp",
      "env": {
        "VIJIL_CLIENT_ID": "${VIJIL_CLIENT_ID}",
        "VIJIL_CLIENT_SECRET": "${VIJIL_CLIENT_SECRET}",
        "VIJIL_TEAM_ID": "${VIJIL_TEAM_ID}"
      }
    }
  }
}
```

## Trust Score

- Three dimensions: **Reliability** (correctness, consistency, robustness), **Security** (confidentiality, integrity, availability), **Safety** (containment, compliance, transparency).
- **Scale differs by surface.** The Console and reports show 0 to 100 (70 or more passes). The SDK returns 0.0 to 1.0 (`score.summarize(..., scale=100)` converts). Use `0.70` as the SDK equivalent of 70.
- A dimension that cannot be scored shows no score and is left out of the overall Trust Score. Treat `trust_score is None` as a failure in a gate.

## Quick Reference

### SDK

```python
import os
from vijil import Vijil

client = Vijil()  # reads credentials, gateway, and team as described above

agent = client.agents.create(
    name="My Chat Agent",
    url="https://api.openai.com/v1/chat/completions",  # must be OpenAI chat-completions compatible
    model_name="gpt-4o",
    api_key=os.environ["OPENAI_API_KEY"],
    protocol="chat_completions",                         # or "a2a"
)

evaluation = client.evaluate(agent.id, baseline=True, sample_size=50)  # blocks and polls
print(evaluation.trust_score, evaluation.dimensions.security)

results = client.scores.results(evaluation.id)
failures = client.evaluations.responses(evaluation.id, status="failed")
pdf_bytes = client.reports.download(evaluation.id)  # generates the report if missing
```

Lifecycle methods on the client:

| Method | Purpose |
|--------|---------|
| `evaluate(agent_id, baseline=True \| harness_id=..., sample_size=, type="behavioral" \| "redteam", redteam={...})` | Run and wait for an evaluation. `baseline` and `harness_id` are mutually exclusive; `redteam` rejects both and `sample_size` |
| `protect(agent_id, policy_id=, guards=, mode="enforce" \| "monitor" \| "disabled")` | Create or update the agent's Dome config |
| `adapt(agent_id, mode="config" \| "code")` | Ask Darwin for improvement proposals |
| `discover(github_org= \| github_repo= \| provider="aws" \| "k8s")` | Find agents |
| `register(path)` | Register a local agent directory (5 MiB, 500 files max) |
| `evolve(...)`, `deploy(agent_id, runtime=...)` | Darwin evolution and deployment |

Resources: `agents`, `evaluations` (including `redteam_status`, `seeds`, `attacks`, `judgments`, `reflections`, `report`, `report_pdf`), `harnesses`, `scores`, `reports`, `dome`, `policies` (`extract_rules`, `rules`), `personas`, `proposals`, `genomes`, `jobs`, `monitor`, `agent_tunnel`. `client.test()` was removed; use `client.evaluate()`.

Errors subclass `VijilError`: `VijilAuthError` (401/403), `VijilNotFoundError` (404), `VijilValidationError` (400/422), `VijilRateLimitError` (429), `VijilServerError` (5xx), `VijilNetworkError`, `VijilJobFailedError`, `VijilConfigError`.

### MCP Tools

| Area | Tools |
|------|-------|
| Status and teams | `vijil_status`, `team_list`, `team_use` |
| Agents | `agent_create`, `agent_list`, `agent_get`, `agent_update`, `agent_archive`, `agent_lifecycle` |
| Harnesses | `harness_list`, `harness_custom_create`, `harness_custom_get`, `harness_custom_prompts` |
| Evaluations | `eval_run` (`agent_id`, `harness_names`, `sample_size` 1 to 1000, `harness_type`, `wait`), `eval_status`, `eval_results_detail`, `eval_responses`, `eval_report`, `eval_cancel` |
| Red Team | `eval_redteam_status`, `eval_redteam_seeds`, `eval_redteam_attacks`, `eval_redteam_judgments`, `eval_redteam_reflections`, `eval_redteam_report`, `eval_redteam_report_pdf` |
| Personas and Policies | `persona_preset_list`, `persona_from_preset`, `persona_create`, `policy_preset_list`, `policy_from_preset`, `policy_create`, `policy_activate`, `policy_add_rule` |
| Dome | `dome_default_config`, `dome_config_create`, `dome_config_update`, `dome_config_apply`, `dome_detect` |

### REST API

| Operation | Request |
|-----------|---------|
| Register an agent | `POST /v1/agent-configurations/` with `agent_name`, `model_name`, `agent_url`, `api_key`, `protocol` |
| Start an evaluation | `POST /v1/evaluations/` with `agent_id`, `team_id`, `type` (`behavioral` or `redteam`), `harness_names`, `harness_type`, `sample_size`, or `redteam: {max_waves}`. Returns 202 and an evaluation ID |
| Check status | `GET /v1/evaluations/{id}` |
| Summary and results | `GET /v1/evaluation-summaries/{id}?team_id=`, `GET /v1/evaluation-results/{id}/results?team_id=` |
| Responses | `GET /v1/evaluations/{id}/responses?team_id=&status=failed` |
| Report | `POST /v1/evaluations/{id}/report?team_id=`, then `GET /v1/evaluations/{id}/pdf?team_id=` |
| Red Team detail | `GET /v1/evaluations/{id}/redteam`, `/redteam/attacks`, `/redteam/report` |
| Cancel or delete | `POST /v1/evaluations/{id}/cancel`, `DELETE /v1/evaluations/{id}` |

The full spec is in the API Reference at https://docs.vijil.ai.

### Harnesses

| Harness | Use |
|---------|-----|
| Baseline (`reliability`, `security`, `safety`, or `baseline=True` in the SDK) | Standard Trust Score across the three dimensions |
| Compliance: `eu_ai_act_agent_policy`, `iso42001_agent_policy`, `nist_ai_rmf_agent_policy`, `osfi_e23_agent_policy`, `pipeda_agent_policy`, `sg_pdpa_agent_policy`, `taiwan_ai_basic_act_agent_policy` | Regulation-aligned tests that produce a Compliance Trust Report. Pass `harness_type="standard"`. Do not mix with the baseline Harnesses in one run |
| Custom Harness (`client.harnesses.create(name, agent_id, persona_ids, policy_ids, system_prompt)`) | Tests built from your agent, Personas, and Policies. Immutable once created |

Personas set who talks to the agent (intent `benign`, `curious`, `adversarial`, `malicious`). Policies set the rules it must follow. A Policy must be **Active** before a Harness can use it. `client.policies.extract_rules()` drafts rules from a policy document (50 max); a person approves them in the Console.

### Dome

```python
from vijil_dome import Dome

dome = Dome()  # default Guardrails; or Dome(config_dict) / Dome("guardrails.toml")

scan = dome.guard_input(user_message)
if not scan.is_safe():
    return scan.response_string   # the blocked message
reply = run_agent(user_message)
out = dome.guard_output(reply)
```

- **Extras**: `local`, `llm`, `pii`, `full` (local + llm + pii only), `embeddings`, `opentelemetry`, `google`, `s3`, `trust`, `trust-adapters`, `identity`, `controls`, `controls-full`, `strands`, `mcp`. LangChain needs no extra.
- **Guard types**: `security`, `moderation`, `privacy`, `integrity`, `generic`, `policy`. The Console exposes security, moderation, and privacy.
- **Common Detectors**: `prompt-injection-mbert`, `prompt-injection-deberta-v3-base`, `security-promptguard`, `encoding-heuristics`, `moderation-deberta`, `moderation-flashtext`, `moderations-oai-api`, `privacy-presidio`, `detect-secrets`, `hhem-hallucination`, `generic-llm`, `policy-sections`.
- **Guardrail keys**: `input-guards`, `output-guards`, `input-early-exit` (default true), `input-run-parallel`, `input-blocked-message`, `input-on-error` (same for `output-`). Each Guard has `type`, `methods`, `early-exit`, `run-parallel`, `on-error`. In TOML, put these under `[guardrail]`.
- **Shadow mode**: `Dome(config, enforce=False)` flags without blocking. `on-error` defaults to fail closed when enforcing and fail open in shadow mode.
- **Console-managed config**: `VijilDome.create_from_api(client_id, client_secret, agent_id, team_id)` enforces the agent's Guards and Controls from the Console. Use `result.guarded_text` when it is not `None`; enforce mode raises `ControlViolationError`. `Dome.create_from_vijil_agent()` is deprecated.
- **Telemetry**: `setup_vijil_telemetry(dome)` sends detections to the Console **Defend** page. It needs the client ID and secret pair; `VIJIL_API_KEY` alone is not enough.
- **Trust Runtime**: `secure_agent(agent, agent_id=..., mode="warn" | "enforce")` for LangGraph, Google ADK, and Strands.
- **Framework integrations**: Google ADK model callbacks, LangGraph, Strands `DomeHookProvider`, LangChain `GuardrailRunnable`, MCP `DomedMCPServer`.
- **Container**: `ghcr.io/vijilai/vijil-dome-marketplace:latest` on port 80.

## Decision Guidance

| Situation | Do this |
|-----------|---------|
| First look at an agent, no account | Plugin `/vijil inspect` |
| Pre-deployment gate | Baseline behavioral evaluation, fail below 0.70 (SDK) or 70 (Console) |
| Regulated domain | Compliance Harness for the matching regulation |
| Domain-specific behavior | Custom Harness with your Personas and Policies |
| Find attacks a fixed test set misses | `redteam` evaluation (must be enabled on the deployment) |
| Agent runs only on localhost | Expose it with the SDK tunnel (`client.agent_tunnel.get()` plus ngrok) and register with `hub="custom"` |
| Native Anthropic, Bedrock, or Vertex endpoint | Put an OpenAI-compatible adapter in front; Vijil calls chat-completions endpoints |
| Vulnerability found, fix takes time | Add Dome Guards now, fix the root cause, re-evaluate |
| Need to see what Dome would block first | Shadow mode (`enforce=False`) or `mode="monitor"` |

## Workflows

### Evaluate and Gate in CI

1. Store `VIJIL_CLIENT_ID`, `VIJIL_CLIENT_SECRET`, `VIJIL_TEAM_ID`, and `VIJIL_AGENT_ID` as CI secrets.
2. Run `client.evaluate(agent_id, baseline=True)`.
3. Accept only the statuses `completed`, `succeeded`, or `saved`.
4. Fail the job if `trust_score` is `None` or below the threshold (default `0.70`).
5. On failure, read `client.evaluations.responses(id, status="failed")` and the PDF report.

### Evaluate, Protect, Re-Evaluate

1. Register the agent (Console **Agents**, `agent_create`, `client.agents.create`, or `POST /v1/agent-configurations/`).
2. Create Personas and Policies, then a Custom Harness if the baseline is not enough.
3. Run the evaluation and read the failed responses, Failure Patterns, and report.
4. Fix the prompt, tools, or design. Add Dome Guards for the patterns you cannot fix yet (`client.protect` or `dome_config_create`).
5. Re-run the same Harness and compare Trust Scores.

### Discover and Register

1. In the Console, open **Discover > + New Scan**. Add a scan surface (Target) and install a Collector (endpoint, network, Kubernetes, or cloud API) with the one-time enrollment code, or scan a GitHub repository.
2. Review Findings. Classification is `AI`, `Non-AI`, or `Uncertain`.
3. Register an agent-type Resource, then finish registration (endpoint, key, access level). Only **Active** agents can be evaluated.

## Common Gotchas

- **No public CLI.** Older examples with `vijil agent create`, `vijil eval run`, `vijil auth login`, or `vijil config set` are obsolete. Use the SDK, MCP, or REST API.
- **Trust Score scale.** 0 to 100 in the Console, 0.0 to 1.0 in the SDK.
- **Wrong team.** A token can cover several teams, including a personal one. Set `VIJIL_TEAM_ID` explicitly in CI.
- **Long runs.** Evaluations send hundreds of Probes and can take many minutes. Use a small `sample_size` while iterating.
- **Rate limits.** Set `rate_limit_requests_per_minute` on the agent below your model provider's quota.
- **Errored Detectors.** A Detector that cannot score counts as an error, not as a Probe score. The rest of the evaluation still runs.
- **Red Team unavailable.** The Adaptive tab and `type="redteam"` work only when Red Team is enabled for the deployment.
- **Local agents.** Keep the tunnel running for the whole evaluation.
- **Dome first call is slow.** Local Detectors download model weights on first use. Set `VIJIL_MODEL_DIR` to cache them.
- **Custom Harnesses are immutable.** Create a new one to change Personas or Policies.

## Verification Checklist

- [ ] Credentials and `VIJIL_TEAM_ID` are set, and `client.team_id` (or `vijil_status`) shows the expected team
- [ ] Agent is registered, Active, and answers a simple prompt
- [ ] Harness matches the goal (baseline, compliance, custom, or Red Team)
- [ ] Evaluation reached `completed`, `succeeded`, or `saved`, not `failed` or `degraded`
- [ ] Trust Score meets the threshold on the right scale
- [ ] Failed responses and the report were reviewed
- [ ] Dome Guards were tested against known attacks and false positives
- [ ] The agent was re-evaluated after fixes

## Resources

- Page index: https://docs.vijil.ai/llms.txt
- Trust Score: https://docs.vijil.ai/concepts/trust-score/introduction
- Developer quickstart: https://docs.vijil.ai/developer-guide/agentic/quickstart
- Claude Code plugin: https://docs.vijil.ai/developer-guide/getting-started/claude-code-plugin
- SDK reference: https://docs.vijil.ai/developer-guide/sdk/setup
- MCP tools: https://docs.vijil.ai/developer-guide/agentic/tools
- Running evaluations: https://docs.vijil.ai/developer-guide/evaluate/running-evaluations
- Dome: https://docs.vijil.ai/developer-guide/protect/overview
