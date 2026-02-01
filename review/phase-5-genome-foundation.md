# Phase 5: Genome Foundation

[← Back to Index](index.md) | [← Phase 4](phase-4-diamond-a2a-harness.md) | [Next: Phase 6 →](phase-6-darwin-evolution.md)

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Repos** | vijil-console, vijil-console-frontend |
| **PRs** | 3 |
| **Theme** | Genome domain foundation for Darwin |
| **Review Time** | ~1 hour |

This phase establishes the **data layer** that vijil-darwin will use to store and manage agent genomes. No evolution code is included here - that lives in the separate vijil-darwin repository (Phase 6).

---

## Architecture Context

```
┌──────────────────────────────────────────────────────────────────┐
│                    DARWIN ARCHITECTURE                            │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────────────────┐      ┌─────────────────────────┐   │
│  │      vijil-darwin       │      │     vijil-console       │   │
│  │    (evolution engine)   │      │    (data persistence)   │   │
│  │                         │      │                         │   │
│  │  - ConfigOptimizer      │      │  - Genome domain        │   │
│  │  - TrustCubeArchive     │ HTTP │  - GenomeService        │   │
│  │  - EvolutionService     │ ───► │  - GenomeRepository     │   │
│  │  - MutationLogger       │      │  - ProposalRepository   │   │
│  │                         │      │                         │   │
│  └─────────────────────────┘      └─────────────────────────┘   │
│                                                                  │
│  Phase 6: Evolution logic         Phase 5: Data persistence      │
│                                   (this phase)                   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## PR #246 (vijil-console): Genome Foundation

| Attribute | Value |
|-----------|-------|
| **Linear Issues** | CON-170, CON-171, CON-172, CON-173, CON-174 |
| **Lines Changed** | +15,220 / -2 |
| **Files** | 40 |

### What's Included

This is a "squashed" PR containing four sub-issues:

| Issue | Layer | Content |
|-------|-------|---------|
| CON-171 | Domain | `Genome`, `Gene`, `GeneGroup` models + ports |
| CON-172 | Database | SQLAlchemy models + 3 migrations |
| CON-173 | Repository | `GenomeRepository`, `ProposalRepository` |
| CON-174 | Service/API | `GenomeService`, `GenomeRouter`, DI wiring |

### Domain Models

```python
# Core genome model
class Genome(BaseModel):
    id: UUID
    agent_id: UUID
    team_id: UUID
    version: int
    genes: dict[str, GeneGroup]
    fitness_scores: dict[str, float]  # reliability, security, safety
    parent_version: int | None
    created_at: int

# Gene group (logical grouping)
class GeneGroup(BaseModel):
    name: str  # "llm", "tools", "behavior"
    genes: list[Gene]

# Individual gene (mutable property)
class Gene(BaseModel):
    name: str
    type: GeneType  # TEXT, BOOLEAN, LIST, OBJECT, NUMERIC
    value: Any
    mutable: bool
    weight: float  # mutation probability weight
```

### Gene Types

| Type | Description | Example |
|------|-------------|---------|
| `TEXT` | String values (prompts) | System prompt, tool descriptions |
| `BOOLEAN` | On/off flags | Memory enabled, delegation enabled |
| `LIST` | Collections | Tools, skills, delegated agents |
| `OBJECT` | Nested config | LLM parameters, guardrail config |
| `NUMERIC` | Numbers | Temperature, max tokens |

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/genomes` | GET | List genomes for team |
| `/genomes` | POST | Create genome for agent |
| `/genomes/{id}` | GET | Get genome by ID |
| `/genomes/{id}` | PUT | Update genome |
| `/genomes/by-agent/{agent_id}` | GET | Get genome by agent |
| `/proposals` | GET | List mutation proposals |
| `/proposals` | POST | Create proposal |
| `/proposals/{id}/approve` | POST | Approve proposal |
| `/proposals/{id}/reject` | POST | Reject proposal |

### Database Schema

**genomes table:**
```sql
CREATE TABLE genomes (
    id UUID PRIMARY KEY,
    agent_id UUID REFERENCES agents(id),
    team_id UUID NOT NULL,
    version INTEGER NOT NULL,
    genes JSONB NOT NULL,
    fitness_scores JSONB,
    parent_version INTEGER,
    created_at BIGINT NOT NULL,
    UNIQUE(agent_id, version)
);
```

**mutation_proposals table:**
```sql
CREATE TABLE mutation_proposals (
    id UUID PRIMARY KEY,
    genome_id UUID NOT NULL,
    genome_version INTEGER NOT NULL,
    team_id UUID NOT NULL,
    agent_id UUID NOT NULL,
    status VARCHAR(50) NOT NULL,  -- pending, evaluating, approved, rejected
    mutations JSONB NOT NULL,
    fitness_before JSONB,
    fitness_after JSONB,
    created_at BIGINT NOT NULL,
    FOREIGN KEY (genome_id, genome_version) REFERENCES genomes(id, version)
);
```

### Key Decisions

**1. Genome vs Agent Configuration**

| Agent Config | Genome |
|--------------|--------|
| Connection details (hub, API key) | Behavioral blueprint |
| User-managed | System-evolved |
| No versioning | Full lineage tracking |
| No fitness | Per-dimension scores |

**2. Fitness Scores per Dimension**

Fitness is stored as a dictionary mapping dimension to score:

```python
fitness_scores = {
    "reliability": 0.85,
    "security": 0.72,
    "safety": 0.91
}
```

This supports the Trust Cube model in Darwin.

**3. Versioning with Parent Reference**

Each genome version tracks its parent:
- `version=1, parent_version=None` (initial)
- `version=2, parent_version=1` (after mutation)
- `version=3, parent_version=2` (after another mutation)

This enables lineage tracking and rollback.

### Files to Focus On

| File | Purpose |
|------|---------|
| `src/domains/genome/models.py` | Domain models (700 lines) |
| `src/domains/genome/ports.py` | Repository interfaces (384 lines) |
| `src/domains/genome/service.py` | Business logic (863 lines) |
| `src/domains/genome/router.py` | REST API (669 lines) |
| `tests/unit/domains/genome/test_models.py` | 25 unit tests |

### Reviewer Checklist

- [ ] Domain models correctly represent genome structure
- [ ] Gene types cover all needed configuration types
- [ ] Repository interfaces are clean and complete
- [ ] Migrations are reversible
- [ ] API endpoints follow existing Console patterns
- [ ] Tests cover key model validation

---

## PR #252 (vijil-console): Mutation History API

| Attribute | Value |
|-----------|-------|
| **Linear Issue** | [CON-185](https://linear.app/vijil/issue/CON-185) |
| **Base Branch** | `feature/genome-foundation` (PR #246) |

**Purpose:** Add endpoint to retrieve mutation history for an agent's genome.

```
GET /genomes/by-agent/{agent_id}/mutation-history
```

**Response:**
```json
{
  "mutations": [
    {
      "version": 3,
      "timestamp": 1706400000,
      "delta": {"dimension": "security", "change": +0.05},
      "rationale": "Added input validation to tool parameters",
      "mutation_type": "GEPA"
    }
  ]
}
```

### Reviewer Checklist

- [ ] Endpoint returns correct mutation history
- [ ] Pagination works correctly
- [ ] Filtering by date range works

---

## PR #42 (vijil-console-frontend): Darwin UI

| Attribute | Value |
|-----------|-------|
| **Linear Issue** | [CON-180](https://linear.app/vijil/issue/CON-180) |

**Purpose:** Agent-centric Darwin evolution experience.

### UI Components

| Component | Description |
|-----------|-------------|
| **Agents Table** | New columns: Trust Score, Readiness |
| **Genome Button** | 🧬 button opens Genome Viewer |
| **Genome Viewer** | Modal showing genome structure, fitness, history |
| **Mutation History** | Timeline of evolutionary changes |

### Key Decision: Agent-Centric Design

Evolution is presented through the lens of agents, not genomes:
- Users see "Agent Trust Score" not "Genome Fitness"
- Evolution happens to agents, genomes are implementation detail
- Power users can dive into genome details via viewer

### Reviewer Checklist

- [ ] Trust Score column displays correctly
- [ ] Genome Viewer shows accurate data
- [ ] Mutation history timeline is readable
- [ ] UI follows existing design patterns

---

## Merge Order

```bash
# 1. Genome foundation (Console)
gh pr merge 246 --squash

# 2. Mutation history API (Console) - depends on #246
gh pr merge 252 --squash

# 3. Darwin UI (Frontend)
gh pr merge 42 --squash
```

---

## Design Documents

For deeper understanding, review these documents:

| Document | Location |
|----------|----------|
| Agent Genome Design | `vijil-console/docs/AGENT_GENOME_DESIGN.md` |
| Darwin Evolution Design | `vijil-console/docs/DARWIN_EVOLUTION_DESIGN.md` |

---

[← Back to Index](index.md) | [← Phase 4](phase-4-diamond-a2a-harness.md) | [Next: Phase 6 →](phase-6-darwin-evolution.md)
