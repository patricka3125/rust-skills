# Rust-Skills

> rust-skills Claude Code


|------|------|
|Skills| 31 |
|Agents| 8 |
|Unsafe| 47 |

---


```
┌─────────────────────────────────────────────────────┐
│ Layer 3: (WHY) │
│ ├── domain-fintech: │
│ ├── domain-web: │
│ ├── domain-cli: │
│ ├── domain-embedded: no_std│
│ ├── domain-cloud-native: │
│ ├── domain-iot: │
│ └── domain-ml: │
├─────────────────────────────────────────────────────┤
│ Layer 2: (WHAT) │
│ ├── m09-domain: DDDvs │
│ ├── m10-performance: │
│ ├── m11-ecosystem: Crate │
│ ├── m12-lifecycle: RAIIDrop│
│ ├── m13-domain-error: │
│ ├── m14-mental-model: │
│ └── m15-anti-pattern: │
├─────────────────────────────────────────────────────┤
│ Layer 1: (HOW) │
│ ├── m01-ownership: │
│ ├── m02-resource: BoxRcArc│
│ ├── m03-mutability: mutCellRefCell│
│ ├── m04-zero-cost: trait│
│ ├── m05-type-driven: NewtypePhantomData│
│ ├── m06-error-handling: ResultErrorpanic │
│ └── m07-concurrency: SendSyncasyncchannel │
└─────────────────────────────────────────────────────┘
```


```
    │
    ▼
┌─────────────────┐
│ Hook │ ← 400+ (/)
│ (UserPromptSubmit)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ rust-router │ ← +
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌───────┐ ┌────────┐
│ Skill │ │ Domain │
└───┬───┘ └────┬───┘
    │          │
    └────┬─────┘
         │
         ▼
┌─────────────────┐
│ UP/DOWN │ ←
└────────┬────────┘
         │
         ▼
┌─────────────────┐
└─────────────────┘
```

---

## Skills (31 )

### Layer 1: (7 )

| Skill | | |
|-------|----------|----------|
| **m01-ownership** | | E0382, E0597, E0506, E0507, E0515, E0716, move, borrow, lifetime |
| **m02-resource** | |Box, Rc, Arc, Weak, RefCell, Cell,|
| **m03-mutability** | |E0596, E0499, E0502, mut,|
| **m04-zero-cost** | |E0277, E0308, E0599, generic, trait,|
| **m05-type-driven** | |PhantomData, newtype, ,|
| **m06-error-handling** | | Result, Option, Error, panic, anyhow, thiserror |
| **m07-concurrency** | | Send, Sync, thread, async, await, Mutex, channel |

### Layer 2: (7 )

| Skill | | |
|-------|----------|--------|
| **m09-domain** | |DDD, , , ,|
| **m10-performance** | |, , flamegraph, criterion|
| **m11-ecosystem** | |Crate , FFI, PyO3, WASM, feature flags|
| **m12-lifecycle** | |RAII, Drop, , OnceCell|
| **m13-domain-error** | |, ,|
| **m14-mental-model** | |Rust, ,|
| **m15-anti-pattern** | |, ,|

### Layer 3: (7 )

| Skill | | |
|-------|------|----------|
| **domain-fintech** | |, ,|
| **domain-web** |Web|HTTP, ,|
| **domain-cli** | |, TUI, ,|
| **domain-embedded** |/no_std|MCU, , HAL, ,|
| **domain-cloud-native** | |Kubernetes, gRPC, ,|
| **domain-iot** | |MQTT, , ,|
| **domain-ml** | |, ,|

### Skills (10 )

| Skill | |
|-------|------|
| **rust-router** |Rust|
| **rust-learner** |agents Rust/crate|
| **coding-guidelines** |80+ Rust (, , )|
| **unsafe-checker** |47 unsafe , SAFETY , FFI|
| **rust-daily** |Reddit, TWIR, Rust|
| **rust-skill-creator** |skills|
| **core-actionbook** | |
| **core-agent-browser** | |
| **core-dynamic-skills** |Cargo.toml skills|
| **core-fix-skill-docs** |Skill|

---

## Agents (8 )

| Agent | | |
|-------|--------|------|
| **rust-changelog** | releases.rs |Rust ,|
| **crate-researcher** | lib.rs, crates.io |Crate , , features|
| **docs-researcher** | docs.rs |crate API|
| **std-docs-researcher** | doc.rust-lang.org | |
| **clippy-researcher** | rust-clippy |Lint ,|
| **rust-daily-reporter** | Reddit, TWIR, Blog |(//)|
| **browser-fetcher** | WebFetch | |


```
1. actionbook MCP →
2. agent-browser CLI →
3. WebFetch →
```

---


|------|------|
| `/rust-router` |skill|
| `/guideline [--clippy] rule` | |
| `/skill-index category` |skills|
| `/docs crate [item]` |API|


|------|------|
| `/rust-features [version]` |Rust /|
| `/crate-info crate` |Crate|
| `/rust-daily [day\|week\|month]` | |


|------|------|
| `/unsafe-check file` |unsafe|
| `/unsafe-review file` |unsafe|
| `/rust-review file` |clippy|
| `/audit [security\|safety\|concurrency\|full]` | |


|------|------|
| `/cache-status [--verbose]` | |
| `/cache-clean [--all\|--expired\|crate]` | |

### Skill

|------|------|
| `/sync-crate-skills [--force]` |Cargo.toml skills|
| `/update-crate-skill crate` |crate skill|
| `/clean-crate-skills [--all]` |skills|
| `/create-skills-via-llms crate path` |llms.txt skill|
| `/create-llms-for-skills urls` |URL llms.txt|
| `/fix-skill-docs [--check-only]` |skill|

---

## Unsafe (47 )


|------|--------|--------|
|FFI| 10 |C , ABI, extern|

### SAFETY

```rust
// SAFETY: [] []
unsafe {
}
```

---


|------|--------|------|

---

## (_meta/)

|------|------|
| **reasoning-framework.md** | |
| **layer-definitions.md** |L1/L2/L3|
| **error-protocol.md** |3-Strike|
| **externalization.md** | |
| **hooks-patterns.md** | |

---

## Hook


|------|------|

### Hook

1. **** → L1 L3 skills

---


|------|-----|------|
| Crates | 24h |Crate|
|Rust| 168h | |
| Clippy Lints | 168h |Lint|


- Stale-while-revalidate

---


### Rust

```toml
[package]
edition = "2024"
rust-version = "1.85"

[lints.rust]
unsafe_code = "warn"

[lints.clippy]
all = "warn"
pedantic = "warn"
```


```json
{
  "name": "rust-skills",
  "version": "1.0.0",
  "skills": "./skills/",
  "hooks": "./hooks/hooks.json"
}
```

---


- Layer 1 skill ()
- Layer 3 skill ()

### 3. Skill

Cargo.toml crate skills

### 4. Agents

8 agents

### 5. Unsafe

47 FFI


---


****: "Web API Rc cannot be sent between threads"

```
Arc Rc
```

```
+-- Layer 1: Send/Sync
|       ^
+-- Layer 3: Web (domain-web)
| : Handlers
|       v
+-- Layer 2:
    : Arc<T> + State extractor

domain-web:
- "Rc in state"
- Web handlers Send + Sync
- : axum State<Arc<T>>

[axum State extractor Arc
Web ]
```

---


**rust-skills** Claude Rust **Rust **

4. **** agents

