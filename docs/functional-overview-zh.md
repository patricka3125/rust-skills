# Rust-Skills


|------|---------|---------|
|Skills|Dynamic Skills|Skills crate skills|


---

## 1. (Meta-Cognition)


> Claude Code Rust ****


|------|---------|-----------|

### Skills


| Skill | |
|-------|------|
| **rust-router** | |
| **_meta/reasoning-framework** | |
| **_meta/layer-definitions** |L1/L2/L3|

#### Layer 1: (HOW)

Rust

| Skill | | |
|-------|--------|----------|
| **m01-ownership** | | E0382, E0597, move, borrow |
| **m02-resource** | |Box, Rc, Arc,|
| **m03-mutability** | | E0499, E0502, mut, Cell |
| **m04-zero-cost** | | E0277, generic, trait |
| **m05-type-driven** | | newtype, PhantomData |
| **m06-error-handling** | | Result, Error, panic |
| **m07-concurrency** | | Send, Sync, async |

#### Layer 2: (WHAT)


| Skill | |
|-------|--------|
| **m09-domain** | |
| **m10-performance** | |
| **m11-ecosystem** | |
| **m12-lifecycle** | |
| **m13-domain-error** | |
| **m14-mental-model** | |
| **m15-anti-pattern** | |

#### Layer 3: (WHY)


| Skill | | |
|-------|------|----------|
| **domain-fintech** | | |
| **domain-web** | Web | |
| **domain-cli** | | |
| **domain-embedded** | |no_std|
| **domain-cloud-native** | | |
| **domain-iot** | | |
| **domain-ml** | | |


```
: "Web API Rc cannot be sent"
    │
    ▼
┌─────────────────────────────────────────┐
│ rust-router │
│ ├─ : "Web API" → : domain-web │
│ ├─ : "Send" → : m07 │
└─────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────┐
│ L1: Rc Send () │
│  ↑                                       │
│ L3: Web handlers () │
│  ↓                                       │
│ L2: Arc + State extractor () │
└─────────────────────────────────────────┘
    │
    ▼
```

---

## 2. Skills (Dynamic Skills)


> Rust crateskillsClaude Code ****crate skills


|------|----------|
|Crate| |


```
~/.claude/skills/ ← (crate)
├── tokio/
│   ├── SKILL.md
│   └── references/
├── serde/
├── ratatui/
└── std/ ←

/.claude/skills/ ← ()
├── sqlx/
├── sea-orm/
└── my-company-crate/
```


|------|----------|------|
|crate|`~/.claude/skills/`| tokio, serde, ratatui, std |

### Skills

| Skill | |
|-------|------|
| **core-dynamic-skills** |skills|
| **rust-skill-creator** |skills|


|------|------|
| `/sync-crate-skills` |Cargo.toml|
| `/update-crate-skill <crate>` |crate|
| `/clean-crate-skills` |skills|
| `/create-llms-for-skills <urls>` |URL llms.txt|
| `/create-skills-via-llms <crate> <path>` |llms.txt skill|


```
Cargo.toml
┌─────────────────────────────────────────┐
│ /sync-crate-skills                      │
│     │                                    │
│     ▼                                    │
│ Cargo.toml │
│     │                                    │
│     ▼                                    │
│ actionbook llms.txt │
│     │                                    │
│ ├─ → skill │
│ └─ → docs.rs │
│     │                                    │
│     ▼                                    │
│ ~/.claude/skills/{crate}/ │
└─────────────────────────────────────────┘

crate
┌─────────────────────────────────────────┐
│ /create-llms-for-skills <docs_url>      │
│     │                                    │
│     ▼                                    │
│ llms.txt │
│     │                                    │
│     ▼                                    │
│ /create-skills-via-llms tokio ./llms.txt│
│     │                                    │
│     ▼                                    │
│ skill │
└─────────────────────────────────────────┘
```

### Skill

```
~/.claude/skills/tokio/
├── SKILL.md # skill
└── references/ #
    ├── runtime.md
    ├── task.md
    ├── sync.md
    └── io.md
```

### Skill

crate****

```
~/.claude/skills/
├── tokio/ # Skill:
│   ├── SKILL.md
│   └── references/
│ └── rust-defaults.md ←
│
├── tokio-task/ # Skill:
│   └── references/ → symlink
├── tokio-sync/
└── tokio-time/
```

- `rust-defaults.md`
- Skill

`docs/architecture-zh.md` "Skill "

---

## 3. (Info Fetching)


> Claude Code Rust ****Rust


|------|----------|

### Skills

| Skill | |
|-------|------|
| **rust-learner** |crate|
| **rust-daily** |Rust|

### Agents ()

| Agent | | |
|-------|--------|----------|
| **rust-changelog** | releases.rs |Rust|
| **crate-researcher** | lib.rs, crates.io |Crate features|
| **docs-researcher** | docs.rs |crate API|
| **std-docs-researcher** | doc.rust-lang.org | |
| **clippy-researcher** | rust-clippy |Lint|
| **rust-daily-reporter** | Reddit, TWIR, Blog | |


|------|------|
| `/rust-features [version]` |Rust|
| `/crate-info <crate>` |crate|
| `/docs <crate> [item]` |API|
| `/rust-daily [day\|week\|month]` |Rust|


```
┌─────────────────────────────────────────────────────────┐
├─────────────────────────────────────────────────────────┤
│                                                          │
│ Rust Rust │
│  ┌──────────────┐            ┌──────────────┐           │
│  │ releases.rs  │            │ crates.io    │           │
│ │ │ │ lib.rs │ │
│  └──────┬───────┘            └──────┬───────┘           │
│         │                           │                    │
│  ┌──────┴───────┐            ┌──────┴───────┐           │
│  │doc.rust-lang │            │ docs.rs      │           │
│ ││ │ crate │ │
│  └──────────────┘            └──────────────┘           │
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │ Reddit       │  │ TWIR         │  │ Blog         │   │
│ │ r/rust │ │ This Week │ │ │ │
│  └──────────────┘  └──────────────┘  └──────────────┘   │
│                                                          │
└─────────────────────────────────────────────────────────┘
```


|----------|-----|------|
|Rust| 168h | |
|Crate| 24h | |
|API| 72h | |
| Clippy Lints | 168h |Rust|


```
: "tokio "
    │
    ▼
┌─────────────────────────────────────────┐
│ rust-learner │
│ : crate → crate-researcher │
└─────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────┐
│ crate-researcher agent                   │
│ 1. (24h TTL) │
│ 2. lib.rs │
│ 3. : featureschangelog │
└─────────────────────────────────────────┘
    │
    ▼
crate
```

### rust-learner

`rust-learner` **Skill**Agents

```
        │
        ▼
┌───────────────────────────────────────────┐
│ rust-learner () │
│                                            │
│ → Agent → │
└───────────────────────────────────────────┘
        │
        ├──────────────────┬──────────────────┐
        ▼                  ▼                  ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│rust-changelog│  │crate-        │  │docs-         │
│              │  │researcher    │  │researcher    │
│ releases.rs  │  │ lib.rs       │  │ docs.rs      │
└──────────────┘  └──────────────┘  └──────────────┘
```

**Agent **:

|----------|--------------|--------|
|Crate /| `crate-researcher` | lib.rs, crates.io |
|(Send, Arc...)| `std-docs-researcher` | doc.rust-lang.org |
|Clippy lint| `clippy-researcher` | rust-clippy |


```
latest version, what's new, changelog, Rust 1.x,
crate info, docs.rs, API documentation, which crate

crate
```


|------|------|
|** WebSearch**|WebSearch crate|
|**Fallback **| actionbook → agent-browser → WebFetch |

### Actionbook MCP

**Actionbook** rust-skills ****

#### Actionbook

```
(Actionbook):
┌─────────────────────────────────────────────────────────┐
│ 1. lib.rs │
│ 2. HTML (100KB+) │
│ 3. DOM│
│ 5. ... tokens │
└─────────────────────────────────────────────────────────┘

Actionbook:
┌─────────────────────────────────────────────────────────┐
│ 1. actionbook: "lib.rs crate info" │
│    {                                                     │
│      "version": ".crate-version",                       │
│      "description": ".crate-description",               │
│      "features": ".crate-features li"                   │
│    }                                                     │
└─────────────────────────────────────────────────────────┘
```

#### Actionbook

```
┌─────────────────────────────────────────────────────────┐
│                    Actionbook MCP                        │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ lib.rs:                                          │    │
│  │   version: ".crate-version"                      │    │
│  │   features: ".crate-features li"                 │    │
│  │                                                  │    │
│  │ docs.rs:                                         │    │
│  │   signature: ".fn-signature"                     │    │
│  │   description: ".docblock"                       │    │
│  │                                                  │    │
│  │ releases.rs:                                     │    │
│  │   changelog: ".release-notes"                    │    │
│  │   features: ".language-features li"              │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│ MCP │
│ ├── search_actions(query) → │
│ └── get_action_by_id(id) → │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**MCP **:

|------|------|------|
| `search_actions` | query, type, limit |action IDs, ,|
| `get_action_by_id` | id |URL, ,|


|------|---------------|---------------|
|**Token **|( HTML)|()|

**rust-skills Actionbook **:

```
rust-learner
    ├── crate-researcher → actionbook: lib.rs
    ├── docs-researcher → actionbook: docs.rs
    ├── rust-changelog → actionbook: releases.rs
    └── std-docs-researcher → actionbook: doc.rust-lang.org
```

### agent-browser

**agent-browser** Actionbook

```bash
agent-browser open <url> #
agent-browser get text <selector> # actionbook
agent-browser close #
```


|------|------|
| `open <url>` | |
| `snapshot -i` |( ref)|
| `get text <selector>` | |
| `click @ref` | |
| `fill @ref "text"` | |
| `screenshot` | |


```
┌─────────────────────────────────────────────────────────┐
├─────────────────────────────────────────────────────────┤
│                                                          │
│ Layer 1: (rust-learner) │
│  ┌─────────────────────────────────────────────────┐    │
│ │ : "tokio " │ │
│ │ : crate → crate-researcher agent │ │
│  └─────────────────────────────────────────────────┘    │
│                          │                               │
│                          ▼                               │
│ Layer 2: (Actionbook MCP) │
│  ┌─────────────────────────────────────────────────┐    │
│  │ search_actions("lib.rs crate")                   │    │
│  │ get_action_by_id("lib.rs/crates")               │    │
│ │ : { version: ".crate-version", ... } │ │
│  └─────────────────────────────────────────────────┘    │
│                          │                               │
│                          ▼                               │
│ Layer 3: (agent-browser) │
│  ┌─────────────────────────────────────────────────┐    │
│  │ agent-browser open lib.rs/crates/tokio          │    │
│  │ agent-browser get text ".crate-version"         │    │
│  └─────────────────────────────────────────────────┘    │
│                          │                               │
│                          ▼                               │
│ : tokio 1.49.0, features, │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Fallback**:

```
actionbook MCP → agent-browser CLI → WebFetch ()
     │                  │                │
     ▼                  ▼                ▼
```


|------|------|------|
| Actionbook + agent-browser | | |
| WebFetch | | |

---


```
┌─────────────────────────────────────────────────────────┐
└─────────────────────────┬───────────────────────────────┘
                          │
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
    ┌───────────┐   ┌───────────┐   ┌───────────┐
    │ │ │ Skills│ │ │
    │           │   │           │   │           │
    │ │ │ crate │ │ │
    └─────┬─────┘   └─────┬─────┘   └─────┬─────┘
          │               │               │
          └───────────────┼───────────────┘
                          │
                          ▼
            ┌─────────────────────────┐
            └─────────────────────────┘
```


****: "tokio 1.40 Web "

```
1. : Web + → domain-web + m07
2. Skills: tokio skill (API )
3. : tokio 1.40

→ : tokio Web
```

---


|--------|----------|---------------|
|** Skills**| | core-dynamic-skills, rust-skill-creator |

**rust-skills **

Claude Code ************Rust
