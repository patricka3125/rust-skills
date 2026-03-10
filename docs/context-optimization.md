# Context Optimization Guide

> Rust Skills


Rust Skills **68%** token

|---------|------|---------|---------|
| **Skill ** |  | skill | 50-60% |
| **context: fork** |  | skill | 75-85% |

---

## Skill


Skill SKILL.md

### rust-guru

|------|--------|--------|------|
| Token | ~4,700 | ~2,000 | **~2,700 tokens** |


```
skills/
├── SKILL.md (8.1KB - )
├── patterns/
│ └── negotiation.md ()
├── examples/
│ └── workflow.md ()
└── integrations/
    └── os-checker.md ()
```


|------|--------|------|
| Negotiation Protocol | `patterns/negotiation.md` | 4.5 KB |
| Workflow Example | `examples/workflow.md` | 2.3 KB |
| OS-Checker Integration | `integrations/os-checker.md` | 1.3 KB |
| Skill File Paths |  | 1.5 KB |


Claude Code frontmatter `description`

```yaml
---
name: rust-guru
description: "CRITICAL: Use for ALL Rust questions...
Triggers on: Rust, cargo, rustc, E0382, E0597..."
---
```

SKILL.md body ****


- Skill
- Skill
- /Skill

---

## context: fork


`context: fork` Skill subagent


```yaml
---
name: my-task-skill
description: "Task description"
context: fork
agent: general-purpose # Explore
---
```


| Skill | Token | Fork |  |
|-------|---------------|----------------|------|
| `rust-skill-creator` | ~3,000 | ~500 () | **~83%** |
| `core-dynamic-skills` | ~2,000 | ~400 | **~80%** |
| `core-fix-skill-docs` | ~1,500 | ~300 | **~80%** |
| `rust-daily` | ~2,500 | ~500 | **~80%** |

### Fork

|------|------|


```
(Main Context)
├── CLAUDE.md ─────────────► ✅ ()
├── skills ────────► ✅
```


---

## Fork


layer analyzer


```
User Question
     │
     ▼
meta-cognition-parallel ()
     │
     ├─── Fork → layer1-analyzer ──► L1
     │
     ├─── Fork → layer2-analyzer ──► L2 []
     │
     └─── Fork → layer3-analyzer ──► L3
     │
     ▼
Cross-Layer Synthesis ()
     │
```


```
├── m01-ownership +1,200 tokens
├── m02-resource +1,000 tokens
├── domain-fintech +1,500 tokens
├── +2,500 tokens
└── +1,800 tokens
                          ────────────
                          ~8,000 tokens
```

**Fork:**
```
├── L1 +600 tokens
├── L2 +600 tokens
├── L3 +600 tokens
└── ++700 tokens
                          ────────────
                          ~2,500 tokens
```


- `skills/meta-cognition-parallel/SKILL.md` - Skill
- `agents/layer1-analyzer.md` - (m01-m07)
- `agents/layer2-analyzer.md` - (m09-m15)
- `agents/layer3-analyzer.md` - (domain-*)


```bash
/meta-parallel <your Rust question>
```


```bash
/meta-parallel E0382trade record move

# 2: Web API
/meta-parallel Web API handler

# 3: CLI
/meta-parallel CLI
```

---


Rust

|------|--------|--------|
| rust-guru | 4,700 | 2,000 |
| skill | 8,000 | 2,500 |

---


```
    │
    ├── Skill?
    │ └── YES → :
    │
    │ └── YES → : context: fork
    │ context: fork frontmatter
    │
        └── YES → : Fork
                  meta-cognition-parallel
```

---


- SKILL.md
- `examples/`
- `integrations/`
- `references/`

### 2. Fork

- Skill fork
- /Skill fork
- fork


- fork

---


- [ ] rust-guru
  ```bash
  claude -p "E0382 "
  claude -p "tokio async-std"
  ```


- [ ] Fork skill
  ```bash
  /sync-crate-skills
  /rust-daily
  ```


  ```bash
  /meta-parallel E0382
  ```

---


|------|------|---------|
| 2.0.0 | 2025-01-22 | rust-guru (56% ) |
| 2.0.4 | 2025-01-22 | 4 skills context: fork (thanks @pinghe) |
| 2.0.5 | 2025-01-22 | Fork |

---

**Created:** 2025-01-21
**Updated:** 2025-01-22
**Status:** ✅ Implemented (Methods 1-3)
