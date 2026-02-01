# Phase 2: Diamond Bug Fixes

[← Back to Index](index.md) | [← Phase 1](phase-1-dome-bugfix.md) | [Next: Phase 3 →](phase-3-small-enhancements.md)

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Repo** | [vijil-diamond](https://github.com/vijilAI/vijil-diamond) |
| **PRs** | [#95](https://github.com/vijilAI/vijil-diamond/pull/95), [#100](https://github.com/vijilAI/vijil-diamond/pull/100) |
| **Theme** | Scoring accuracy improvements |
| **Review Time** | ~30 minutes |

---

## PR #95: Exclude detector errors from scoring

| Attribute | Value |
|-----------|-------|
| **Linear Issue** | [DIAMOND-60](https://linear.app/vijil/issue/DIAMOND-60) |
| **Lines Changed** | +20 / -20 |
| **Files** | 2 |

### Problem

When detectors fail (API key errors, timeouts, rate limits), the scoring logic returned `0.0` for probes with no detection results. This **incorrectly penalized the agent** being evaluated for infrastructure failures.

**Example:** During A2A protocol testing, detector 401 errors caused safety scores to drop to 2.4% even though the agent was behaving correctly.

### Solution

Return `float('nan')` instead of `0.0` when:
- No detection results available (all detectors failed)
- No valid scores after filtering

NaN values are **filtered out during aggregation**, so only successful detector runs contribute to the final score.

### Key Code Change

```python
# Before (in 8 locations)
return 0.0

# After
return float('nan')
```

### Key Decision

**Why NaN instead of skipping the probe entirely?**

NaN allows us to:
1. Track that the probe was attempted but failed
2. Filter at aggregation time (not evaluation time)
3. Distinguish "detector failed" from "agent failed"
4. Report on detector health separately from agent scores

### Files Changed

| File | Changes |
|------|---------|
| `src/diamond/vijil_harness_executor/infrastructure/adapters/scoring.py` | 8 locations: `0.0` → `float('nan')` |
| `tests/unit/.../test_scoring.py` | Updated tests to expect NaN for empty inputs |

### Reviewer Checklist

- [ ] All 28 scoring tests pass
- [ ] NaN handling is correct in aggregation code (not in this PR)
- [ ] No downstream code assumes scores are always floats (not NaN)

---

## PR #100: Two-phase evaluation for pairwise detectors

| Attribute | Value |
|-----------|-------|
| **Linear Issue** | [DIAMOND-62](https://linear.app/vijil/issue/DIAMOND-62) |
| **Lines Changed** | +16,177 / -209 |
| **Files** | 63 (includes unrelated ADK/AgentCore work - see note) |

### Important Note

This PR has a large diff because it was based on a feature branch that includes Diamond ADK and AgentCore work. **Focus review on the pairwise evaluation changes only:**

- `src/diamond/vijil_harness_executor/domain/services.py` - Core changes
- `tests/unit/vijil_harness_executor/domain/test_services.py` - New test

### Problem

The `AdvGluePairwiseComparison` detector expects `clean_response` in metadata to compare against the perturbed response. This was **never populated**, causing all 31 AdvGLUE probes to return 0.50 (the default score).

**Impact:** Distributional robustness testing was effectively broken.

### Solution: Two-Phase Evaluation

1. **Phase 1**: Evaluate clean/reference prompts first, store responses
2. **Phase 2**: Pass clean responses as metadata when evaluating perturbed prompts

```
┌────────────────────────────────────────────────────────────────┐
│                   TWO-PHASE EVALUATION                          │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Phase 1: Clean Prompts                                        │
│  ┌──────────┐     ┌─────────┐     ┌──────────────────┐        │
│  │ "What is │ ──► │  Agent  │ ──► │ Response: "The   │        │
│  │ 2 + 2?"  │     │         │     │ answer is 4"     │        │
│  └──────────┘     └─────────┘     └────────┬─────────┘        │
│                                            │                   │
│                                            ▼ Store             │
│  Phase 2: Perturbed Prompts            ┌───────────┐          │
│  ┌──────────┐     ┌─────────┐          │ Reference │          │
│  │ "Wh4t 1s │ ──► │  Agent  │ ◄────────│ Response  │          │
│  │ 2 + 2?"  │     │         │ metadata │           │          │
│  └──────────┘     └─────────┘          └───────────┘          │
│                         │                                      │
│                         ▼                                      │
│               ┌─────────────────┐                              │
│               │ AdvGLUE Detector│  Compare responses           │
│               │  clean_response │  for consistency             │
│               └─────────────────┘                              │
└────────────────────────────────────────────────────────────────┘
```

### Key Code Changes

```python
# New constant mapping detector IDs to metadata keys
PAIRWISE_DETECTOR_CONFIGS = {
    "AdvGluePairwiseComparison": {"reference_key": "clean_response"},
    "AdultDataPairwiseComparison": {"reference_key": "clean_response"},
}

# New methods in HarnessExecutorService
async def _evaluate_pairwise_probe(self, probe, ...) -> ProbeResult:
    """Two-phase evaluation for pairwise detectors."""
    # Phase 1: Get clean response
    clean_response = await self._evaluate_clean_prompt(probe.clean_prompt, ...)

    # Phase 2: Evaluate perturbed with clean response as metadata
    return await self._evaluate_single_prompt_with_metadata(
        probe.prompt,
        metadata={"clean_response": clean_response},
        ...
    )
```

### Key Decision

**Why not fix the data pipeline to include clean responses?**

The probe format doesn't include pre-computed clean responses - they must be obtained at evaluation time from the same agent being tested. Two-phase evaluation is the correct architectural approach.

### Files to Focus On

| File | Purpose |
|------|---------|
| `src/diamond/vijil_harness_executor/domain/services.py` | Core two-phase logic |
| `tests/unit/.../test_services.py` | New test: `test_evaluate_pairwise_probe_two_phase_evaluation` |

### Reviewer Checklist

- [ ] Two-phase evaluation logic is correct
- [ ] Clean response is properly passed as metadata
- [ ] Existing single-prompt evaluation is not affected
- [ ] Test coverage for pairwise evaluation path
- [ ] Ignore other files in diff (ADK/AgentCore - separate feature)

---

## Merge Order

Both PRs target `main` and can be merged independently:

```bash
# PR #95 first (simpler)
gh pr merge 95 --squash

# PR #100 second (larger)
gh pr merge 100 --squash
```

---

[← Back to Index](index.md) | [← Phase 1](phase-1-dome-bugfix.md) | [Next: Phase 3 →](phase-3-small-enhancements.md)
