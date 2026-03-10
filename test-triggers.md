# Rust Skills Trigger Test Checklist

> Run these queries in a project that has rust-skills installed, and verify the correct skill is triggered.

## How to Test

1. Go to a Rust project directory with rust-skills plugin installed
2. Run each query below with `claude -p "query"`
3. Check if the expected skill is triggered (shown in Claude Code status line)

---

## Layer 1: Language Mechanics

## Ownership (m01-ownership)

| Query | Expected Skill |
|-------|----------------|
| `value moved after use` | m01-ownership |
| `borrowed value does not live long enough` | m01-ownership |
| `lifetime annotation` | m01-ownership |
| `E0597 lifetime too short` | m01-ownership |

## Resource (m02-resource)

| Query | Expected Skill |
|-------|----------------|
|`Arc Rc `| m02-resource |
| `Box vs Rc vs Arc` | m02-resource |
|`smart pointer `| m02-resource |
| `shared ownership` | m02-resource |

## Mutability (m03-mutability)

| Query | Expected Skill |
|-------|----------------|
| `E0499 multiple mutable borrows` | m03-mutability |
| `E0502 borrow conflict` | m03-mutability |
| `E0596 cannot borrow as mutable` | m03-mutability |
| `Cell vs RefCell` | m03-mutability |
| `interior mutability` | m03-mutability |

## Zero-Cost (m04-zero-cost)

| Query | Expected Skill |
|-------|----------------|
| `E0277 trait bound not satisfied` | m04-zero-cost |
| `generic vs trait object` | m04-zero-cost |
| `monomorphization` | m04-zero-cost |
| `E0308 type mismatch` | m04-zero-cost |
| `E0282 type annotations needed` | m04-zero-cost |

## Type-Driven (m05-type-driven)

| Query | Expected Skill |
|-------|----------------|
| `newtype pattern` | m05-type-driven |
|`PhantomData `| m05-type-driven |
| `type state pattern` | m05-type-driven |
| `marker trait` | m05-type-driven |

## Error Handling (m06-error-handling)

| Query | Expected Skill |
|-------|----------------|
| `Result vs Option` | m06-error-handling |
|`thiserror `| m06-error-handling |
| `anyhow vs eyre` | m06-error-handling |
| `error propagation` | m06-error-handling |

## Concurrency (m07-concurrency)

| Query | Expected Skill |
|-------|----------------|
| `cannot be sent between threads` | m07-concurrency |
|`async await `| m07-concurrency |
| `Send Sync trait` | m07-concurrency |
|`deadlock `| m07-concurrency |

---

## Layer 2: Design Choices

## Domain Modeling (m09-domain)

| Query | Expected Skill |
|-------|----------------|
| `DDD in Rust` | m09-domain |
|`domain model `| m09-domain |
| `aggregate root` | m09-domain |
| `value object vs entity` | m09-domain |

## Performance (m10-performance)

| Query | Expected Skill |
|-------|----------------|
|`benchmark `| m10-performance |
|`criterion `| m10-performance |
| `cache locality` | m10-performance |
|` zero copy`| m10-performance |

## Ecosystem (m11-ecosystem)

| Query | Expected Skill |
|-------|----------------|
|` crate`| m11-ecosystem |
|`crate `| m11-ecosystem |
|`Cargo.toml `| m11-ecosystem |
|`feature flags `| m11-ecosystem |

## Lifecycle (m12-lifecycle)

| Query | Expected Skill |
|-------|----------------|
| `RAII pattern` | m12-lifecycle |
|`Drop trait `| m12-lifecycle |
|`scopeguard `| m12-lifecycle |

## Domain Error (m13-domain-error)

| Query | Expected Skill |
|-------|----------------|
|`retry `| m13-domain-error |
|`circuit breaker `| m13-domain-error |
|`backoff `| m13-domain-error |

## Mental Model (m14-mental-model)

| Query | Expected Skill |
|-------|----------------|
|` Rust`| m14-mental-model |
|` Java Rust`| m14-mental-model |

## Anti-Pattern (m15-anti-pattern)

| Query | Expected Skill |
|-------|----------------|
| `code smell Rust` | m15-anti-pattern |
|`Rust `| m15-anti-pattern |
|`clone `| m15-anti-pattern |

---

## Core Skills

## Unsafe (unsafe-checker)

| Query | Expected Skill |
|-------|----------------|
|`unsafe `| unsafe-checker |
|`FFI `| unsafe-checker |
| `SAFETY comment` | unsafe-checker |
| `raw pointer` | unsafe-checker |
| `how to call C functions` | unsafe-checker |

## Version/Crate (rust-learner)

| Query | Expected Skill |
|-------|----------------|
|`tokio `| rust-learner |
|`serde `| rust-learner |
| `crate info` | rust-learner |

## Code Style (coding-guidelines)

| Query | Expected Skill |
|-------|----------------|
| `clippy warning` | coding-guidelines |
|`rustfmt `| coding-guidelines |
| `P.NAM.01` | coding-guidelines |

## Router (rust-router)

| Query | Expected Skill |
|-------|----------------|

## Layer 3: Domain Constraints

## Domains

| Query | Expected Skill |
|-------|----------------|
| `kubernetes operator in Rust` | domain-cloud-native |
|`decimal `| domain-fintech |
|` tensor`| domain-ml |
| `IoT sensor` | domain-iot |
| `axum web server` | domain-web |
| `clap CLI argument` | domain-cli |
| `no_std embedded` | domain-embedded |

---

## Quick Test Commands

```bash
# Layer 1: Language Mechanics
claude -p "E0382 " # m01-ownership
claude -p "E0499 multiple mutable borrows" # m03-mutability
claude -p "newtype pattern"              # m05-type-driven
claude -p "Send Sync trait"              # m07-concurrency

# Layer 2: Design Choices
claude -p "DDD in Rust"                  # m09-domain
claude -p "benchmark " # m10-performance
claude -p "crate" # m11-ecosystem
claude -p "RAII pattern"                 # m12-lifecycle
claude -p "circuit breaker " # m13-domain-error
claude -p "Rust" # m14-mental-model
claude -p "Rust " # m15-anti-pattern

# Core Skills
claude -p "unsafe " # unsafe-checker
claude -p "tokio " # rust-learner
claude -p "Rust " # coding-guidelines

# Layer 3: Domains
claude -p "axum web server"              # domain-web
claude -p "decimal " # domain-fintech
```

## Expected Behavior

When a skill triggers correctly, you should see:
1. The skill name in Claude Code's status line
2. Response content that matches the skill's expertise
3. References to patterns/rules from that skill

## Troubleshooting

If skills don't trigger:
1. Ensure rust-skills plugin is installed: `claude /plugins`
2. Check plugin path is correct
3. Verify SKILL.md files have `description:` field with keywords
4. Try more specific keywords from the skill description
