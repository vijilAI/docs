# Phase 4: Diamond A2A Protocol + Trust Harness

[← Back to Index](index.md) | [← Phase 3](phase-3-small-enhancements.md) | [Next: Phase 5 →](phase-5-genome-foundation.md)

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Repo** | [vijil-diamond](https://github.com/vijilAI/vijil-diamond) |
| **PRs** | 6 (2 stacks) |
| **Theme** | A2A protocol support + Harness quality improvements |
| **Review Time** | ~1.5 hours |

This phase has two independent work streams that can be reviewed in parallel:

1. **A2A Protocol Stack** (4 PRs): Diamond can evaluate A2A agents
2. **Trust Harness Stack** (3 PRs): Encoding-as-variant restructuring

---

## Part A: A2A Protocol Stack

### Architecture Overview

```
┌──────────────────────────────────────────────────────────────────┐
│                    DIAMOND A2A EVALUATION                         │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────────┐                    ┌────────────────┐       │
│  │  Diamond API   │                    │  Diamond ADK   │       │
│  │  (REST server) │                    │  (A2A server)  │       │
│  └───────┬────────┘                    └───────┬────────┘       │
│          │                                     │                 │
│          │  Creates evaluation                 │  A2A protocol   │
│          ▼                                     ▼                 │
│  ┌────────────────────────────────────────────────────┐         │
│  │              A2AAgentProvider                       │         │
│  │                                                     │         │
│  │  - JSON-RPC over HTTP                              │         │
│  │  - Task streaming                                   │         │
│  │  - Agent Card discovery                            │         │
│  └────────────────────────────────────────────────────┘         │
│                            │                                     │
│                            ▼                                     │
│                   ┌───────────────┐                              │
│                   │   A2A Agent   │  (any A2A-compatible agent)  │
│                   │   Endpoint    │                              │
│                   └───────────────┘                              │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### PR #82: Diamond ADK (base)

| Attribute | Value |
|-----------|-------|
| **Branch** | `diamond-adk` → `main` |
| **Lines Changed** | +13,339 / -163 |

**Purpose:** Complete Diamond ADK module that wraps `vijil_harness_executor` as a Google ADK agent with A2A protocol support.

**Key Features:**

| Feature | Description |
|---------|-------------|
| **Tools** | `evaluate`, `list_probes`, `get_agent_info` |
| **CLI** | `python -m diamond.adk` starts A2A server on port 8081 |
| **LLM Support** | Configurable (Gemini default, also OpenAI/Anthropic) |
| **Local Harnesses** | `LocalHarnessLoader` reads from vijil_objects JSONL |
| **Storage** | Pluggable (filesystem default, also S3, GCP, DigitalOcean) |
| **Validation** | Pydantic models with structured error responses |

**New Module Structure:**

```
src/diamond/adk/
├── __init__.py      # Package exports
├── __main__.py      # CLI entry point
├── agent.py         # ADK agent definition
├── agent_card.py    # A2A agent card generation
├── config.py        # Configuration management
├── exceptions.py    # Custom exception hierarchy
├── models.py        # Pydantic request/response models
├── server.py        # A2A server wrapper
├── telemetry.py     # OpenTelemetry instrumentation
└── tools.py         # evaluate, list_probes, get_agent_info
```

**Key Decision: Filesystem Storage**

Added `FilesystemStorage` adapter for local development:
- Results stored in `~/.diamond/storage/`
- No cloud credentials required
- Same interface as S3 storage

### PR #83: Diamond AgentCore

| Attribute | Value |
|-----------|-------|
| **Branch** | `diamond-agentcore` → `diamond-adk` |
| **Lines Changed** | +12 commits on top of #82 |

**Purpose:** Diamond variant for AWS Bedrock AgentCore deployment.

**Key Features:**
- FastAPI server with `/invoke` and `/stream` endpoints
- Bedrock AgentCore configuration (`.bedrock_agentcore.yaml`)
- Docker deployment support

**New Module:**

```
src/diamond/agentcore/
├── __init__.py
├── __main__.py      # Uvicorn entry point
├── config.py        # Bedrock configuration
├── models.py        # Request/response models
└── server.py        # FastAPI application
```

### PR #86: Sample Size Parameter

| Attribute | Value |
|-----------|-------|
| **Branch** | `feat/sample-size-gepa` → `main` |
| **Focus** | GEPA optimization support |

**Purpose:** Add `sample_size` parameter to control probes per harness during evaluation.

**Use Case:** GEPA (Guided Evolution Prompt Adaptation) needs fast evaluation cycles with fewer probes to iterate quickly on prompt optimization.

```python
# Full evaluation: ~1000 probes × 3 harnesses = 3000 probes (~10 min)
# Sampled:         50 probes × 3 harnesses = 150 probes (~30 sec)
```

### PR #89: Protocol-based Provider Selection

| Attribute | Value |
|-----------|-------|
| **Branch** | `feat/agent-protocol-field` → `diamond-adk` |
| **Linear Issue** | [DIAMOND-55](https://linear.app/vijil/issue/DIAMOND-55) |

**Purpose:** Select agent provider based on `protocol` field from Console.

**Key Change:**

```python
def get_agent_provider(config: AgentConfig) -> AgentProvider:
    if config.protocol == "a2a":
        return A2AAgentProvider(config)
    else:
        return ChatCompletionsProvider(config)  # default
```

### A2A Stack Merge Order

```bash
# Merge in order (each builds on previous)
gh pr merge 82 --squash  # diamond-adk → main
gh pr merge 83 --squash  # diamond-agentcore → main (after #82)
gh pr merge 86 --squash  # sample_size → main
gh pr merge 89 --squash  # protocol field → main (after #82)
```

---

## Part B: Trust Harness v0.0.6 - v0.1.0

### Problem Statement

The current trust harness (v0.0.5) has **53 encoding probes** (28% of total) that create redundancy and score noise:

| Issue | Impact |
|-------|--------|
| Encoding treated as scenarios | Inflated scenario count (14 → effectively 9 unique) |
| Standalone encoding tests | Score pollution (encoding success ≠ safety success) |
| No combination testing | Can't test "harmful prompt + encoding" together |

### Solution: Encoding-as-Variant

Treat encoding as a **cross-cutting concern** that applies to probes, not as standalone scenarios.

```
BEFORE (v0.0.5):
┌─────────────────────────────────────────────────────┐
│ Scenarios: harmful_content, encoding_leetspeak,    │
│            encoding_base64, encoding_homoglyph,    │
│            injection, encoding_zero_width, ...     │
└─────────────────────────────────────────────────────┘

AFTER (v0.1.0):
┌─────────────────────────────────────────────────────┐
│ Scenarios: harmful_content, injection, ...         │
│                                                     │
│ Variants: plain, leetspeak, base64, homoglyph,    │
│           zero_width, rot13                        │
└─────────────────────────────────────────────────────┘
```

### PR #104: Encoding-as-Variant Infrastructure (DIAMOND-63)

| Attribute | Value |
|-----------|-------|
| **Linear Issue** | [DIAMOND-63](https://linear.app/vijil/issue/DIAMOND-63) |

**Purpose:** Build the infrastructure for variant-based evaluation.

**Key Components:**

| Component | Purpose |
|-----------|---------|
| `EncodingVariant` enum | `PLAIN`, `LEETSPEAK`, `BASE64`, `HOMOGLYPH`, `ZERO_WIDTH`, `ROT13` |
| `VariantProbe` model | Probe with `variant` field |
| `VariantEncoder` | Applies encoding to prompt text |
| `VariantScorer` | Weighted scoring across variants |

**Scoring Model:**

```python
# Weighted average across variants
final_score = sum(variant_scores * weights) / sum(weights)

# Default weights (configurable)
VARIANT_WEIGHTS = {
    "plain": 1.0,      # Full weight for unmodified
    "leetspeak": 0.5,  # Half weight for encoded
    "base64": 0.5,
    # ...
}
```

### PR #105: New Scenarios (DIAMOND-64)

| Attribute | Value |
|-----------|-------|
| **Linear Issue** | [DIAMOND-64](https://linear.app/vijil/issue/DIAMOND-64) |

**Purpose:** Add three new scenario types addressing coverage gaps:

| Scenario | Gap Addressed | Description |
|----------|---------------|-------------|
| **Consistency** | Response stability | Same question phrased differently should get consistent answers |
| **Instruction Hierarchy** | System vs user prompt priority | System prompt should override conflicting user instructions |
| **Misinformation** | Factual accuracy | Agent should not state false facts confidently |

### PR #106: Encoding Migration (DIAMOND-65)

| Attribute | Value |
|-----------|-------|
| **Linear Issue** | [DIAMOND-65](https://linear.app/vijil/issue/DIAMOND-65) |

**Purpose:** Migrate 53 existing encoding probes to variant model.

**Migration Steps:**
1. Extract encoding probes from standalone scenarios
2. Convert to variant format
3. Attach to parent probes (e.g., harmful content + leetspeak variant)
4. Remove deprecated standalone scenarios

### Trust Harness Stack Merge Order

```bash
# Merge in order (stacked PRs)
gh pr merge 104 --squash  # encoding-as-variant infrastructure
gh pr merge 105 --squash  # new scenarios (depends on #104)
gh pr merge 106 --squash  # encoding migration (depends on #105)
```

---

## Reviewer Checklist

### A2A Protocol
- [ ] A2AAgentProvider correctly implements JSON-RPC protocol
- [ ] Agent Card discovery works for remote endpoints
- [ ] Error handling for unreachable agents
- [ ] Filesystem storage works without cloud credentials
- [ ] Protocol field routes to correct provider

### Trust Harness
- [ ] Variant infrastructure doesn't break existing evaluation
- [ ] Weighted scoring produces reasonable results
- [ ] New scenarios have appropriate probes
- [ ] Encoding migration preserves probe coverage

---

[← Back to Index](index.md) | [← Phase 3](phase-3-small-enhancements.md) | [Next: Phase 5 →](phase-5-genome-foundation.md)
