# Phase 6: Darwin Evolution System

[← Back to Index](index.md) | [← Phase 5](phase-5-genome-foundation.md)

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Repo** | [vijil-darwin](https://github.com/vijilAI/vijil-darwin) (NEW) |
| **PRs** | 9 (stacked) |
| **Theme** | Complete evolution engine |
| **Review Time** | ~2 hours |

This is the **main Darwin feature** - a complete agent evolution engine in a new standalone repository. Darwin improves AI agent behavior by:

1. **Observing** security/safety violations detected by Dome
2. **Proposing** genome mutations based on violation patterns
3. **Evaluating** mutations with Diamond to verify improvement
4. **Applying** verified improvements after human approval

---

## Pre-Reading: Design Document

**Read this first:** [`vijil-console/docs/plans/2026-01-25-darwin-genome-evolution-design.md`](https://github.com/vijilAI/vijil-console/blob/main/docs/plans/2026-01-25-darwin-genome-evolution-design.md)

Key concepts to understand:
- **Trust Cube**: 3D behavioral space (Reliability × Security × Safety)
- **MAP-Elites**: Quality-diversity algorithm that maintains diverse elite solutions
- **GEPA**: Guided Evolution Prompt Adaptation (prompt optimization)
- **IC-QD**: In-context Quality-Diversity (config optimization via LLM)

---

## Architecture

```
┌──────────────────────────────────────────────────────────────────────────┐
│                         VIJIL-DARWIN SERVICE                              │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                      API Server (FastAPI)                         │   │
│  │  /evolution/run, /evolution/status, /evolution/proposals         │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                    │                                     │
│                                    ▼                                     │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                     EvolutionService                              │   │
│  │  Orchestrates: observe → propose → evaluate → apply               │   │
│  └───────────────────────────┬──────────────────────────────────────┘   │
│                              │                                           │
│         ┌────────────────────┼────────────────────┐                     │
│         ▼                    ▼                    ▼                     │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐               │
│  │ ConfigOpti- │     │ TrustCube   │     │ Mutation    │               │
│  │ mizer (IC-QD)│     │ Archive     │     │ Logger      │               │
│  │             │     │ (pyribs)    │     │ (S3)        │               │
│  └─────────────┘     └─────────────┘     └─────────────┘               │
│         │                    │                    │                     │
│         └────────────────────┼────────────────────┘                     │
│                              │                                           │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                    HTTP Adapters                                  │   │
│  │  ConsoleClient (genomes), DiamondClient (evaluations)            │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                              │                                           │
└──────────────────────────────┼───────────────────────────────────────────┘
                               ▼
                    ┌──────────────────┐      ┌──────────────────┐
                    │  vijil-console   │      │  vijil-diamond   │
                    │  (Genome CRUD)   │      │  (Evaluation)    │
                    └──────────────────┘      └──────────────────┘
```

---

## PR Stack Overview

| PR | Title | Lines | Component |
|----|-------|-------|-----------|
| [#2](https://github.com/vijilAI/vijil-darwin/pull/2) | MutationRecord domain model | +257 | Data model |
| [#3](https://github.com/vijilAI/vijil-darwin/pull/3) | MutationLogger for S3 | +1,917 | Persistence |
| [#4](https://github.com/vijilAI/vijil-darwin/pull/4) | TrustCubeArchive (pyribs) | +909 | MAP-Elites grid |
| [#5](https://github.com/vijilAI/vijil-darwin/pull/5) | IC-QD prompt builder/parser | +461 | LLM prompts |
| [#6](https://github.com/vijilAI/vijil-darwin/pull/6) | ConstraintResolver | +377 | Dynamic constraints |
| [#7](https://github.com/vijilAI/vijil-darwin/pull/7) | ConfigOptimizer (IC-QD) | +2,777 | Core optimizer |
| [#8](https://github.com/vijilAI/vijil-darwin/pull/8) | HTTP adapters | +1,086 | External clients |
| [#9](https://github.com/vijilAI/vijil-darwin/pull/9) | EvolutionService | +764 | Orchestration |
| [#10](https://github.com/vijilAI/vijil-darwin/pull/10) | API Server | +491 | FastAPI routes |

**Total:** ~9,000 lines of new code

---

## PR #2: MutationRecord Domain Model

| Attribute | Value |
|-----------|-------|
| **Linear Issue** | [VIJIL-573](https://linear.app/vijil/issue/VIJIL-573) |
| **Lines** | +257 |

**Purpose:** Data structure for capturing mutation context, action, and outcome for future model distillation.

```python
@dataclass
class MutationRecord:
    """Training data for distillation."""

    # Context (input to future model)
    archive_summary: str          # Current state of elite archive
    parent_genome: dict           # Genome being mutated
    behavioral_target: tuple[float, float, float]  # Desired niche
    objective: str                # "improve security while maintaining reliability"

    # Mutation (output to predict)
    proposed_mutation: dict       # What the LLM proposed
    mutation_rationale: str       # Why (chain of thought)

    # Outcome (reward signal)
    fitness_before: float
    fitness_after: float
    behavior_achieved: tuple[float, float, float]
    placed_in_archive: bool       # Did it become an elite?
```

**Key Decision:** Record both successes AND failures - failed mutations are informative for distillation.

---

## PR #3: MutationLogger for S3

| Attribute | Value |
|-----------|-------|
| **Linear Issue** | [VIJIL-574](https://linear.app/vijil/issue/VIJIL-574) |
| **Lines** | +1,917 |

**Purpose:** Persist MutationRecords to S3 for future model distillation.

**S3 Path Structure:**
```
teams/{team_id}/darwin/mutations/
├── 2026-01-25T12:00:00_mutation_abc123.json
├── 2026-01-25T12:05:00_mutation_def456.json
└── ...
```

**Key Decision:** Use `StoragePort` protocol for dependency injection - allows filesystem storage during development.

---

## PR #4: TrustCubeArchive (pyribs)

| Attribute | Value |
|-----------|-------|
| **Linear Issue** | [VIJIL-575](https://linear.app/vijil/issue/VIJIL-575) |
| **Lines** | +909 |

**Purpose:** MAP-Elites archive using [pyribs](https://pyribs.org/) library.

**Trust Cube Grid:**
```
Reliability: [0.0-0.2, 0.2-0.4, 0.4-0.6, 0.6-0.8, 0.8-1.0]
Security:    [0.0-0.2, 0.2-0.4, 0.4-0.6, 0.6-0.8, 0.8-1.0]
Safety:      [0.0-0.2, 0.2-0.4, 0.4-0.6, 0.6-0.8, 0.8-1.0]

Total: 5 × 5 × 5 = 125 niches
```

**Key Method:**
```python
def summarize_for_llm(self) -> str:
    """Generate LLM-friendly archive context for IC-QD prompts."""
    return f"""
    Current archive state:
    - Cell (4,3,2): fitness=0.85, genome={{tools: [search, calc], memory: true}}
    - Cell (3,4,3): fitness=0.82, genome={{tools: [search], memory: false}}
    - [12 more elites...]
    """
```

---

## PR #5: IC-QD Prompt Builder/Parser

| Attribute | Value |
|-----------|-------|
| **Linear Issue** | [VIJIL-576](https://linear.app/vijil/issue/VIJIL-576) |
| **Lines** | +461 |

**Purpose:** Structured prompts for LLM-guided mutations.

**Prompt Template:**
```
Current archive state:
{archive_summary}

Parent genome (from cell {cell}):
{genome_json}

Target: Improve {target_dimension} score while maintaining {constraint_dimension} > {threshold}

Constraints:
- tools: max 5 items, allowed: [search, calc, email, calendar, ...]
- memory: boolean

Propose a single mutation. Format:
GENE: <gene_name>
ACTION: ADD | REMOVE | MODIFY
VALUE: <new_value>
RATIONALE: <why this helps>
```

**Response Parser:** Extracts `ParsedMutation(gene_name, action, value, rationale)` from LLM output.

---

## PR #6: ConstraintResolver

| Attribute | Value |
|-----------|-------|
| **Linear Issue** | [VIJIL-577](https://linear.app/vijil/issue/VIJIL-577) |
| **Lines** | +377 |

**Purpose:** Fetch valid options for list-type genes from Agent Registry.

```python
class ConstraintResolver:
    async def resolve(self, gene_name: str) -> GeneConstraints:
        if gene_name == "tools":
            # Query Agent Registry for available tools
            tools = await self.agent_service.list_available_tools()
            return GeneConstraints(max_length=5, allowed_items=tools)
```

**Key Decision:** Dynamic constraints from Agent Registry (not hardcoded) - allows tenant-specific tool catalogs.

---

## PR #7: ConfigOptimizer (IC-QD)

| Attribute | Value |
|-----------|-------|
| **Linear Issue** | [VIJIL-578](https://linear.app/vijil/issue/VIJIL-578) |
| **Lines** | +2,777 |

**Purpose:** Core LLM-guided mutation engine.

**Algorithm:**
```python
async def optimize(self, genome: Genome, iterations: int = 10) -> Genome:
    for i in range(iterations):
        # 1. Select target niche (exploration vs exploitation)
        target_cell = self.archive.select_target()

        # 2. Generate mutation via LLM
        prompt = self.prompt_builder.build(
            genome=genome,
            archive=self.archive.summarize_for_llm(),
            target=target_cell
        )
        response = await self.llm.generate(prompt)
        mutation = self.parser.parse(response)

        # 3. Validate mutation
        if not self.constraint_resolver.validate(mutation):
            continue

        # 4. Apply mutation to genome
        mutated_genome = genome.apply_mutation(mutation)

        # 5. Evaluate with Diamond
        fitness = await self.diamond.evaluate(mutated_genome)

        # 6. Try to add to archive
        self.archive.add(mutated_genome, fitness)

        # 7. Log for distillation
        self.logger.log(MutationRecord(...))

    return self.archive.best_genome()
```

---

## PR #8: HTTP Adapters

| Attribute | Value |
|-----------|-------|
| **Linear Issue** | [VIJIL-579](https://linear.app/vijil/issue/VIJIL-579) |
| **Lines** | +1,086 |

**Purpose:** HTTP clients for Console and Diamond APIs.

**ConsoleClient:**
```python
class ConsoleClient:
    async def get_genome(self, agent_id: UUID) -> Genome
    async def update_genome(self, genome: Genome) -> Genome
    async def create_proposal(self, proposal: MutationProposal) -> MutationProposal
```

**DiamondClient:**
```python
class DiamondClient:
    async def evaluate(self, genome: Genome) -> EvaluationResult
    async def get_fitness_scores(self, evaluation_id: UUID) -> dict[str, float]
```

---

## PR #9: EvolutionService

| Attribute | Value |
|-----------|-------|
| **Linear Issue** | [VIJIL-580](https://linear.app/vijil/issue/VIJIL-580) |
| **Lines** | +764 |

**Purpose:** Orchestrate the complete evolution workflow.

**Workflow:**
```
observe → propose → evaluate → apply

1. OBSERVE: Poll Dome for detection events
2. PROPOSE: Generate mutations based on violations
3. EVALUATE: Run Diamond evaluation on mutated genome
4. APPLY: Save improved genome (requires human approval)
```

---

## PR #10: API Server

| Attribute | Value |
|-----------|-------|
| **Linear Issue** | [VIJIL-579](https://linear.app/vijil/issue/VIJIL-579) |
| **Lines** | +491 |

**Purpose:** FastAPI server with evolution endpoints.

**Endpoints:**

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/evolution/run` | POST | Start evolution run for agent |
| `/evolution/status/{run_id}` | GET | Get run status and progress |
| `/evolution/proposals` | GET | List pending proposals |
| `/evolution/proposals/{id}/approve` | POST | Approve mutation proposal |

---

## Merge Order

**Critical:** These PRs are stacked - merge in order!

```bash
cd vijil-darwin

# Each PR builds on the previous
gh pr merge 2 --squash   # MutationRecord
gh pr merge 3 --squash   # MutationLogger
gh pr merge 4 --squash   # TrustCubeArchive
gh pr merge 5 --squash   # IC-QD prompt
gh pr merge 6 --squash   # ConstraintResolver
gh pr merge 7 --squash   # ConfigOptimizer
gh pr merge 8 --squash   # HTTP adapters
gh pr merge 9 --squash   # EvolutionService
gh pr merge 10 --squash  # API Server
```

---

## Key Decisions Summary

| # | Decision | Rationale |
|---|----------|-----------|
| 1 | Separate repo (vijil-darwin) | Clean domain boundary, mirrors vijil-diamond pattern |
| 2 | pyribs for MAP-Elites | Battle-tested library, active maintenance |
| 3 | LLM-guided mutations | More intelligent than random perturbation |
| 4 | Log all mutations (success + failure) | Failures inform future distillation |
| 5 | Dynamic constraints from Agent Registry | Tenant-specific tool catalogs |
| 6 | Human approval required for apply | Safety checkpoint before production |

---

## Reviewer Checklist

### Domain Models (PR #2)
- [ ] MutationRecord captures all needed fields for distillation
- [ ] Serialization handles UUIDs and tuples correctly

### Persistence (PR #3)
- [ ] StoragePort protocol is clean
- [ ] S3 path structure is logical
- [ ] Error handling for storage failures

### Archive (PR #4)
- [ ] pyribs integration is correct
- [ ] 5×5×5 grid configuration is appropriate
- [ ] `summarize_for_llm()` produces useful context

### Optimizer (PR #5-7)
- [ ] Prompt template is clear and actionable
- [ ] Response parser handles edge cases
- [ ] Constraint validation prevents invalid mutations
- [ ] ConfigOptimizer algorithm is sound

### Integration (PR #8-10)
- [ ] HTTP clients handle errors gracefully
- [ ] EvolutionService workflow is correct
- [ ] API endpoints follow REST conventions
- [ ] Authentication/authorization is handled

---

## Strategic Context

**Why Darwin matters:**

1. **Data Flywheel**: Phase 2 (IC-QD) generates mutation data → distill specialized LLM → Phase 3: low-cost agent generation

2. **Two Market Motions**:
   - **Tune existing agents**: Code + detections → Improved agent
   - **Generate from spec**: Spec + policies → Complete safe agent (larger market)

3. **Competitive Moat**: Proprietary "Darwin Agent Architect" trained on real mutation outcomes

---

[← Back to Index](index.md) | [← Phase 5](phase-5-genome-foundation.md)
