# Rust-Skills

> Skills


```
┌─────────────────────────────────────────────────────────────────────┐
└─────────────────────────────────┬───────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│ Hook │
│  hooks/hooks.json + .claude/hooks/rust-skill-eval-hook.sh           │
└─────────────────────────────────┬───────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│ (rust-router) │
└───────────┬─────────────────────────────────┬───────────────────────┘
            │                                 │
            ▼                                 ▼
┌───────────────────────┐       ┌───────────────────────────────────┐
│ Skills │ │ Skills │
│                        │       │                                    │
│ skills/ │ │ ~/.claude/skills/ () │
│  ├── m01-m07 (L1)     │       │  ├── tokio/                        │
│  ├── m09-m15 (L2)     │       │  ├── serde/                        │
│  ├── domain-* (L3)    │       │  └── std/                          │
│  ├── rust-router      │       │                                    │
│ ├── coding-guidelines│ │ .claude/skills/ () │
│  └── unsafe-checker   │       │  └── project-specific-crate/       │
└───────────┬───────────┘       └───────────────┬───────────────────┘
            │                                   │
            └─────────────┬─────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────────┐
│ Agents │
│  agents/                                                             │
│ ├── rust-changelog (Rust ) │
│ ├── crate-researcher (Crate ) │
│ ├── docs-researcher (API ) │
│ └── rust-daily-reporter () │
└─────────────────────────────────┬───────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│ - (Reasoning Chain) │
└─────────────────────────────────────────────────────────────────────┘
```

---


```
rust-skills/
│
├── .claude-plugin/
│ └── plugin.json # (name, skills, hooks)
│
├── .claude/
│   ├── hooks/
│ │ └── rust-skill-eval-hook.sh #
│ └── settings.json #
│
├── hooks/
│ └── hooks.json # Hook (400+ )
│
├── skills/ # Skills
│   │
│ ├── rust-router/ #
│   │   └── SKILL.md
│   │
│ ├── m01-ownership/ # Layer 1:
│   ├── m02-resource/
│   ├── m03-mutability/
│   ├── m04-zero-cost/
│   ├── m05-type-driven/
│   ├── m06-error-handling/
│   ├── m07-concurrency/
│   │
│ ├── m09-domain/ # Layer 2:
│   ├── m10-performance/
│   ├── m11-ecosystem/
│   ├── m12-lifecycle/
│   ├── m13-domain-error/
│   ├── m14-mental-model/
│   ├── m15-anti-pattern/
│   │
│ ├── domain-fintech/ # Layer 3:
│   ├── domain-web/
│   ├── domain-cli/
│   ├── domain-embedded/
│   ├── domain-cloud-native/
│   ├── domain-iot/
│   ├── domain-ml/
│   │
│ ├── coding-guidelines/ #
│ ├── unsafe-checker/ # Unsafe
│ ├── rust-learner/ #
│ ├── rust-daily/ #
│   │
│ ├── core-dynamic-skills/ # Skill
│ ├── core-actionbook/ #
│ ├── core-agent-browser/ #
│ └── core-fix-skill-docs/ #
│
├── agents/ # Agents
│   ├── rust-changelog.md
│   ├── crate-researcher.md
│   ├── docs-researcher.md
│   ├── std-docs-researcher.md
│   ├── clippy-researcher.md
│   ├── rust-daily-reporter.md
│   └── browser-fetcher.md
│
├── commands/ #
│   ├── rust-features.md
│   ├── crate-info.md
│   ├── sync-crate-skills.md
│   └── ...
│
├── _meta/ #
│   ├── reasoning-framework.md
│   ├── layer-definitions.md
│   ├── error-protocol.md
│   ├── externalization.md
│   └── hooks-patterns.md
│
├── cache/ #
│   ├── config.yaml
│   ├── crates/
│   ├── rust-versions/
│   └── docs/
│
├── docs/ #
│   ├── capabilities-summary.md
│   ├── capabilities-summary-zh.md
│   ├── functional-overview-zh.md
│   ├── architecture-zh.md
│   ├── what-is-a-skill.md
│   ├── problem-solved.md
│   └── skills-design-lessons.md
│
└── templates/ #
    ├── trace.md
    ├── findings.md
    └── decision.md
```

---

## Skill

### SKILL.md

```yaml
---
name: skill-name
description: "CRITICAL: Use for [purpose]. Triggers on: keyword1, keyword2, ..."
globs: ["**/*.rs"] #
---

# Skill

> Layer X:

## Core Question

## Error → Design Question

## Trace Up ↑

## Trace Down ↓

## Quick Reference

## Common Errors / Anti-Patterns

## Related Skills
```

### description ()

```yaml
description: "CRITICAL: Use for [purpose]. Triggers on: keyword1, keyword2, ..."

description: "A skill for handling ownership"
```

---


### 1. Hook → Router → Skills

```
hooks/hooks.json
    │
    ▼
.claude/hooks/rust-skill-eval-hook.sh
    │
    ▼
skills/rust-router/SKILL.md
    │
    ▼
skills/m0x-* + skills/domain-*
```

### 2. Skills vs Skills

```
┌─────────────────────────────────────────────────────────┐
│                    Claude Code                           │
├─────────────────────────────────────────────────────────┤
│                                                          │
│ Skills (rust-skills/) Skills │
│  ┌────────────────────┐         ┌────────────────────┐  │
│  │ skills/            │         │ ~/.claude/skills/  │  │
│ │ - │ │ - tokio │ │
│ │ - │ │ - serde │ │
│ │ - │ │ - std │ │
│  └────────────────────┘         └────────────────────┘  │
│                                                          │
│                                  ┌────────────────────┐  │
│                                  │ .claude/skills/    │  │
│                                  │ - sqlx             │  │
│                                  │ - sea-orm          │  │
│                                  └────────────────────┘  │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### 3. Agents Skills

```
Skills () Agents ()
       │                         │
       │                         │
       ▼                         ▼
┌─────────────┐           ┌─────────────┐
│ rust-learner│ ────────► │ crate-      │
│ () │ │ researcher │
└─────────────┘           └─────────────┘
       │                         │
       │                         │
       ▼                         ▼
┌─────────────┐           ┌─────────────┐
└─────────────┘           └─────────────┘
       │                         │
       └───────────┬─────────────┘
                   │
                   ▼
            ┌─────────────┐
            └─────────────┘
```

---


```
   "Web API Rc cannot be sent"
        │
        ▼
2. Hook (hooks/hooks.json)
   : "Web API", "Rc", "Send"
        │
        ▼
3. Hook (rust-skill-eval-hook.sh)
        │
        ▼
4. Router (rust-router)
   : L1 = m07-concurrency
         L3 = domain-web
        │
        ▼
5. Skill
   Skill(m07-concurrency) → Send/Sync
   Skill(domain-web) → Web
        │
        ▼
   L1: Rc Send
    ↑
   L3: Web handlers
    ↓
   L2: Arc + State extractor
        │
        ▼
   - (Web )
```

---


### 1. Skill

|------|------|
|** (Core Question)**| |
|** (Trace Up/Down)**| |

### 2. Description

```yaml
description: "CRITICAL: Use for concurrency. Triggers on: Send, Sync, async, thread, E0277"

description: "CRITICAL: Use for ownership. Triggers on: E0382, borrow, "

description: "Helps with Rust ownership"

description: "CRITICAL: Use for errors"
```


```
skills/
├── domain-web/
├── domain-fintech/
└── m01-ownership/

skills/
├── domains/
│   ├── web/
│   └── fintech/
└── layers/
    └── m01/
```

### 4. Hook

```json
{
  "matcher": "(?i)(Web API|HTTP|axum).*?(Send|Sync|thread)",
  "action": "Load domain-web AND m07-concurrency"
}

{
  "matcher": "E0277",
  "action": "Load m07-concurrency"
}
```


```markdown
+-- Layer 1: Send/Sync
|       ^
+-- Layer 3: Web
|       v
+-- Layer 2:

[domain-web ]


Arc Rc
```

### 6. Skills

|------|----------|
|crate (tokio, serde, std)| `~/.claude/skills/` |

### 7. Skill

crate**Skill**

```
~/.claude/skills/
├── tokio/ # Skill ()
│ ├── SKILL.md #
│   └── references/
│ └── rust-defaults.md #
│
├── tokio-task/ # Skill ()
│   ├── SKILL.md
│   └── references/
│       └── rust-defaults.md  → symlink to ../tokio/references/
│
├── tokio-sync/ # Skill
├── tokio-time/ # Skill
├── tokio-io/ # Skill
└── tokio-net/ # Skill
```

**Skill** (`tokio/SKILL.md`):

```yaml
---
name: tokio
description: |
  CRITICAL: Use for tokio async runtime questions. Triggers on:
  tokio, spawn, select!, join!, mpsc, timeout, sleep, ...
---
# crate
# Skills
```

**Skill** (`tokio-task/SKILL.md`):

```yaml
---
name: tokio-task
description: |
  CRITICAL: Use for tokio task management. Triggers on:
  tokio::spawn, JoinHandle, JoinSet, spawn_blocking, abort, ...
---
```

**** (`references/rust-defaults.md`):

```markdown
# Rust Code Generation Defaults

## Cargo.toml Defaults
edition = "2024" # Skill

## Common Dependencies
| Crate | Version |
|-------|---------|
| tokio | 1.49    |

## Code Style
...
```


|------|----------|


```bash
# 1. Skill
~/.claude/skills/tokio/SKILL.md
~/.claude/skills/tokio/references/rust-defaults.md

# 2. Skillssymlink
cd ~/.claude/skills/tokio-task/references
ln -s ../../tokio/references/rust-defaults.md .

# 3. Skill
# SKILL.md
# **IMPORTANT: Before generating any Rust code,
#  read `./references/rust-defaults.md` for shared rules.**
```

### 8. Agent

```
# - rust-learner
/crate-info tokio


# - WebSearch
WebSearch Rust/crate
```

---


### Layer 1 Skill

```markdown
---
name: m08-new-skill
description: "CRITICAL: Use for [topic]. Triggers on: keyword1, keyword2"
---

# New Skill Title

> Layer 1: Language Mechanics

## Core Question

## Trace Up ↑

## Trace Down ↓
```

### Domain Skill

```markdown
---
name: domain-new
description: "CRITICAL: Use for [domain]. Triggers on: keyword1, keyword2"
---

# Domain Name

> Layer 3: Domain Constraints

## Domain Constraints → Design Implications

## Trace Down ↓
```

### Agent

```markdown
# agent-name.md

## Purpose

## Data Source

## Output Format

## Cache Strategy
```

---


|------|------|------|


1. **Skills **
2. **Layer 1**
6. **Skills **
7. **Agents **
