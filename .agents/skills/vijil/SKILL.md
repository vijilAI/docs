---
name: Vijil
description: Use when evaluating AI agents for trustworthiness (reliability, security, safety), running adversarial tests before deployment, configuring runtime protection with guardrails, integrating trust gates into CI/CD pipelines, or generating audit-ready trust reports for compliance.
metadata:
    mintlify-proj: vijil
    version: "1.0"
---

# Vijil Skill

## Product Summary

Vijil is a trust platform for AI agents that measures and enforces trustworthiness across three dimensions: **Reliability** (does it do the right thing consistently?), **Security** (can it resist abuse?), and **Safety** (does it stay within policy?). It consists of two products: **Diamond** (evaluation—sends hundreds of adversarial probes and produces a quantified Trust Score 0.0–1.0) and **Dome** (runtime protection—intercepts inputs/outputs and applies configurable guardrails). Access Vijil via the web console at https://evaluate.vijil.ai, the Python SDK (`vijil-console` CLI or `vijil` Python client), or REST API. Key files: agent configurations, harness definitions, evaluation results, guardrail configs. Primary docs: https://docs.vijil.ai

## When to Use

Reach for this skill when:
- **Pre-deployment validation**: You need objective evidence that an agent is safe before shipping (Trust Score gates deployments)
- **Adversarial testing**: You want to probe agent behavior under attack (prompt injection, jailbreaks, data exfiltration)
- **Compliance & audit**: You must document what was tested and provide audit-ready reports
- **Runtime defense**: You've identified vulnerabilities in evaluation and need to block attack patterns in production
- **CI/CD integration**: You want evaluations to run on every PR and gate merges based on Trust Score thresholds
- **Vulnerability remediation**: You've found failures in evaluation and need to verify fixes work
- **Custom evaluation**: You need to test against domain-specific policies, personas, or attack vectors

## Quick Reference

### CLI Commands (vijil-console)

| Task | Command |
|------|---------|
| Initialize CLI | `vijil init --url https://console-api.example.com` |
| Login | `vijil login` |
| Create agent | `vijil agent create --agent-name "Name" --model-name "gpt-4" --api-key "$KEY"` |
| List agents | `vijil agent list` |
| List harnesses | `vijil harness list` |
| Run evaluation | `vijil eval run --agent-id <id> --harness-names '["safety","security"]' --wait` |
| Check status | `vijil eval status <eval_id>` |
| View results | `vijil eval results-detail <eval_id>` |
| Generate report | `vijil eval report <eval_id>` |

### REST API Endpoints

| Operation | Method | Endpoint |
|-----------|--------|----------|
| Authenticate | POST | `/auth/jwt/login` |
| Create agent | POST | `/agent-configurations/` |
| List agents | GET | `/agent-configurations/?limit=10` |
| List harnesses | GET | `/harnesses/?team_id=$TEAM_ID` |
| Run evaluation | POST | `/evaluations/` |
| Check status | GET | `/evaluations/$EVAL_ID` |
| Get results | GET | `/evaluation-results/$EVAL_ID/results` |
| Download report (HTML) | GET | `/evaluations/$EVAL_ID/html` |
| Download report (PDF) | GET | `/evaluations/$EVAL_ID/pdf` |

### Harnesses (Test Suites)

| Harness | Dimensions | Use Case |
|---------|-----------|----------|
| `trust_score` | Reliability, Security, Safety | Comprehensive pre-deployment validation |
| `security` | Security only | Focused security review |
| `reliability` | Reliability only | Quality assurance |
| `safety` | Safety only | Safety review |
| `owasp-llm-top-10` | OWASP Top 10 for LLM Applications | Compliance |
| `*_Small` | Any (add suffix) | Fast iteration during development |

### Trust Score Dimensions

| Dimension | Measures | Example Failures |
|-----------|----------|-----------------|
| **Reliability** | Correctness, consistency, accuracy | Hallucinations, task failures, inconsistent responses |
| **Security** | Resistance to adversarial attacks | Prompt injection, data exfiltration, jailbreaks |
| **Safety** | Policy compliance, ethical boundaries | Harmful content, policy violations, unauthorized actions |

### Dome Guard Types

| Guard Type | Purpose | Example Detectors |
|-----------|---------|-------------------|
| `security` | Block adversarial attacks | `prompt-injection-mbert`, `encoding-heuristics`, `security-embeddings` |
| `moderation` | Filter harmful content | `moderation-flashtext`, `moderation-deberta`, `moderations-oai-api` |
| `privacy` | Prevent data leakage | `privacy-presidio` (PII), `detect-secrets` (credentials) |
| `integrity` | Validate data quality | Format validation (experimental) |
| `generic` | Custom logic | User-defined detectors |

## Decision Guidance

### When to Use Cloud-Hosted vs. Local Evaluation

| Scenario | Use Cloud-Hosted | Use Local |
|----------|------------------|-----------|
| Agent already deployed (OpenAI, Anthropic, Bedrock, etc.) | ✓ | |
| Agent running locally during development | | ✓ |
| Need fast feedback loop without deployment | | ✓ |
| Evaluating production endpoint | ✓ | |
| Testing before any deployment | | ✓ |

### When to Use Specific Harnesses

| Goal | Harness | Reason |
|------|---------|--------|
| Pre-deployment gate (all dimensions) | `trust_score` | Comprehensive coverage |
| Security-focused review | `security` | Faster, targeted testing |
| Compliance with OWASP Top 10 | `owasp-llm-top-10` | Regulatory alignment |
| Fast iteration during development | `*_Small` | Reduced test count, faster results |
| Custom domain-specific testing | Custom harness | Tailored to your policies/personas |

### When to Use Dome vs. Fixing Root Cause

| Situation | Use Dome | Fix Root Cause |
|-----------|----------|----------------|
| Vulnerability found, fix will take weeks | ✓ | Later |
| Need immediate production protection | ✓ | Parallel effort |
| Vulnerability is low-risk, easy to fix | | ✓ |
| Attack pattern is novel/emerging | ✓ | Monitor and iterate |
| Systematic issue in agent design | | ✓ (Dome as interim) |

## Workflow

### Typical Evaluation Workflow

1. **Register your agent**
   - Provide agent name, model name, API key, and endpoint URL
   - CLI: `vijil agent create --agent-name "MyAgent" --model-name "gpt-4" --api-key "$KEY"`
   - API: POST `/agent-configurations/` with agent details

2. **Choose a harness**
   - Start with `trust_score` for comprehensive coverage
   - Use `*_Small` variants for fast iteration
   - Create custom harnesses for domain-specific policies

3. **Run the evaluation**
   - CLI: `vijil eval run --agent-id <id> --harness-names '["trust_score"]' --wait`
   - API: POST `/evaluations/` with agent_id, harness_names, optional sample_size
   - Evaluations run asynchronously; use `--wait` to block or poll status

4. **Monitor progress**
   - CLI: `vijil eval status <eval_id>` (polls every 5 seconds)
   - API: GET `/evaluations/$EVAL_ID` (check status field)
   - Status progression: `starting` → `pending` → `running` → `completed` → `saving` → `saved`

5. **Analyze results**
   - CLI: `vijil eval results-detail <eval_id>`
   - API: GET `/evaluation-results/$EVAL_ID/results`
   - Review Trust Score (0.0–1.0), dimension breakdowns, and individual probe failures

6. **Generate audit report**
   - CLI: `vijil eval report <eval_id>`
   - API: GET `/evaluations/$EVAL_ID/html` or `/pdf`
   - Reports include risk levels, failure examples, implications, and mitigation strategies

7. **Remediate and re-evaluate**
   - Fix vulnerabilities (prompt engineering, system design, guardrails)
   - Re-run evaluation to confirm improvements
   - Track Trust Score over time

### Typical Protection Workflow

1. **Identify vulnerabilities from evaluation**
   - Review evaluation results and failure patterns
   - Prioritize high-risk issues

2. **Configure guardrails**
   - Define input and output guards (security, moderation, privacy)
   - Choose detectors for each guard type
   - Set execution mode (early-exit for speed, parallel for latency)

3. **Deploy Dome**
   - Wrap agent with input/output guardrails
   - Test with sample malicious inputs to verify blocking
   - Monitor scan results and false positives

4. **Monitor and iterate**
   - Log all scans for post-hoc analysis
   - Adjust detector thresholds based on production patterns
   - Plan root-cause fixes while Dome provides interim protection

## Common Gotchas

- **Evaluation takes longer than expected**: Evaluations run hundreds of probes; expect 5–30 minutes depending on harness and agent latency. Use `*_Small` harnesses for faster feedback during development.

- **Trust Score is lower than expected**: Review individual probe failures in results. Common causes: hallucinations (reliability), prompt injection susceptibility (security), policy violations (safety). Fix root causes, not just the score.

- **API key not working**: Verify the key is valid for the provider (OpenAI, Anthropic, etc.). Check rate limits—Vijil has default quotas per provider. Ensure the key has permission for the model you're testing.

- **Local agent evaluation fails with ngrok**: Free plan requires ngrok token. Premium users don't need it. If using free plan, export `NGROK_AUTHTOKEN` before running evaluation.

- **Dome guardrails are too strict**: Start with default configuration, then adjust detector thresholds. Use `early-exit: false` to see all flagged content before blocking. Monitor false positives in production logs.

- **Custom harness not running**: Verify harness is created and associated with your team. Check that personas and policies are defined. Ensure probes are valid.

- **Evaluation status stuck on "running"**: Check agent endpoint is reachable and responding. Verify API key is still valid. If stuck >1 hour, cancel and retry.

- **Report generation fails**: Reports only work for Vijil and custom harnesses, not benchmarks. Ensure evaluation is fully completed (status = `saved`).

- **Guardrail configuration not applied**: Verify config is pushed to agent before requests. Check that guardrail is wrapping the correct input/output points. Confirm detectors are enabled.

## Verification Checklist

Before submitting evaluation results or deploying guardrails:

- [ ] Agent is registered and reachable (test with a simple prompt)
- [ ] Correct harness selected for your use case (trust_score for general, security for focused)
- [ ] Evaluation completed successfully (status = `saved`, not `failed`)
- [ ] Trust Score meets your deployment threshold (e.g., ≥0.70)
- [ ] Reviewed individual failures and understand root causes
- [ ] Generated and reviewed audit report (HTML/PDF)
- [ ] If using Dome: tested guardrails with known attack patterns
- [ ] If using Dome: verified false positive rate is acceptable
- [ ] Documented findings and remediation plan
- [ ] Re-evaluated after fixes to confirm improvement

## Resources

- **Comprehensive page listing**: https://docs.vijil.ai/llms.txt
- **Concepts & Trust Score**: https://docs.vijil.ai/concepts/trust-score/introduction
- **Developer Guide**: https://docs.vijil.ai/developer-guide/getting-started/introduction
- **Evaluation Overview**: https://docs.vijil.ai/developer-guide/evaluate/overview
- **Protection Overview**: https://docs.vijil.ai/developer-guide/protect/overview

---

> For additional documentation and navigation, see: https://docs.vijil.ai/llms.txt