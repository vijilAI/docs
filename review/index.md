# Team Review: Q1 2026 Feature Release

> **Review Period:** February 2026
> **Author:** Vin Sharma
> **Repos:** vijil-dome, vijil-diamond, vijil-console, vijil-console-frontend, vijil-darwin

---

## Overview

This review package covers all pending work across Vijil repositories, organized from smallest (bug fixes) to largest (Darwin evolution system). Each phase builds on previous work, so **review in order**.

### Review Sequence

| Phase | Repo | PRs | Focus | Est. Review Time |
|-------|------|-----|-------|------------------|
| [**Phase 1**](phase-1-dome-bugfix.md) | vijil-dome | 1 | Bug fix: Trust score degradation | 15 min |
| [**Phase 2**](phase-2-diamond-bugfixes.md) | vijil-diamond | 2 | Bug fixes: Scoring accuracy | 30 min |
| [**Phase 3**](phase-3-small-enhancements.md) | vijil-console, frontend | 3 | Small enhancements: A2A, UI | 30 min |
| [**Phase 4**](phase-4-diamond-a2a-harness.md) | vijil-diamond | 6 | Features: A2A protocol, Trust Harness | 1.5 hr |
| [**Phase 5**](phase-5-genome-foundation.md) | vijil-console, frontend | 3 | Feature: Genome domain foundation | 1 hr |
| [**Phase 6**](phase-6-darwin-evolution.md) | vijil-darwin | 9 | Feature: Darwin evolution (new repo) | 2 hr |

**Total estimated review time:** ~6 hours

---

## Architecture Context

### Service Landscape

```
┌─────────────────────────────────────────────────────────────────────┐
│                         VIJIL PLATFORM                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐             │
│  │   Console   │    │   Diamond   │    │    Dome     │             │
│  │  (Backend)  │    │ (Evaluation)│    │ (Guardrails)│             │
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘             │
│         │                  │                  │                     │
│         └──────────────────┼──────────────────┘                     │
│                            │                                        │
│                    ┌───────▼───────┐                                │
│                    │    Darwin     │  ◄── NEW                       │
│                    │  (Evolution)  │                                │
│                    └───────────────┘                                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### What's New

1. **A2A Protocol Support** (Phases 3-4): Diamond can now evaluate agents via Agent-to-Agent JSON-RPC protocol, not just OpenAI chat completions
2. **Trust Harness v0.1.0** (Phase 4): Encoding-as-variant restructuring for cleaner taxonomy
3. **Genome Domain** (Phase 5): Foundation for representing agent behavioral DNA
4. **Darwin Evolution** (Phase 6): Complete evolution engine in new standalone repo

---

## Key Design Documents

Before diving into code, review these design documents:

| Document | Location | Purpose |
|----------|----------|---------|
| Darwin Evolution Design | [`vijil-console/docs/plans/2026-01-25-darwin-genome-evolution-design.md`](https://github.com/vijilAI/vijil-console/blob/main/docs/plans/2026-01-25-darwin-genome-evolution-design.md) | Trust Cube, MAP-Elites, GEPA/IC-QD |
| A2A Protocol Spec | [a2a-protocol.org](https://a2a-protocol.org) | Agent-to-Agent communication standard |

---

## Repository Links

| Repo | Branch | Open PRs |
|------|--------|----------|
| [vijil-dome](https://github.com/vijilAI/vijil-dome) | main | [1 PR](https://github.com/vijilAI/vijil-dome/pulls) |
| [vijil-diamond](https://github.com/vijilAI/vijil-diamond) | main, feature branches | [9 PRs](https://github.com/vijilAI/vijil-diamond/pulls) |
| [vijil-console](https://github.com/vijilAI/vijil-console) | main, feature branches | [5 PRs](https://github.com/vijilAI/vijil-console/pulls) |
| [vijil-console-frontend](https://github.com/vijilAI/vijil-console-frontend) | main | [3 PRs](https://github.com/vijilAI/vijil-console-frontend/pulls) |
| [vijil-darwin](https://github.com/vijilAI/vijil-darwin) | feature/evolution | [9 PRs](https://github.com/vijilAI/vijil-darwin/pulls) |

---

## Linear Project Tracking

| Project | Status | Issues |
|---------|--------|--------|
| [Darwin MVP](https://linear.app/vijil/project/darwin-mvp) | In Progress | VIJIL-539 to VIJIL-553, VIJIL-573 to VIJIL-583 |
| [Diamond Agent](https://linear.app/vijil/project/diamond-agent) | In Progress | DIAMOND-55 to DIAMOND-65 |
| [Config Optimizer (IC-QD)](https://linear.app/vijil/project/config-optimizer) | In Progress | CON-170 to CON-185 |

---

## Merge Order Summary

For clean merges, follow this order:

### 1. vijil-dome (first)
```
#77 → main
```

### 2. vijil-diamond (second)
```
Bug fixes:
  #95 → main
  #100 → main

A2A stack:
  #82 → main (diamond-adk)
  #83 → #82 (diamond-agentcore)
  #86 → main (sample_size)
  #89 → #82 (protocol field)

Trust Harness:
  #104 → main (encoding-as-variant)
  #105 → #104 (new scenarios)
  #106 → #105 (encoding migration)
```

### 3. vijil-console (third)
```
#253 → main (protocol field)
#246 → main (genome foundation)
#252 → #246 (mutation history)
```

### 4. vijil-console-frontend (fourth)
```
#47 → main (contributing guide)
#48 → main (description field)
#42 → main (Darwin UI)
```

### 5. vijil-darwin (last)
```
#2 → feature/evolution (MutationRecord)
#3 → #2 (MutationLogger)
#4 → #3 (TrustCubeArchive)
#5 → #4 (IC-QD prompt)
#6 → #5 (ConstraintResolver)
#7 → #6 (ConfigOptimizer)
#8 → #7 (HTTP adapters)
#9 → #8 (EvolutionService)
#10 → #9 (API Server)
```

---

## Start Review

Begin with [Phase 1: Dome Bug Fix](phase-1-dome-bugfix.md)
