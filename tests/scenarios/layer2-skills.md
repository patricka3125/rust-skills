# Layer 2 Skills Test Scenarios

> Layer 2: Design Choices

## m05-type-driven

| Query | Expected Skill | Expected Elements |
|-------|----------------|-------------------|
| `newtype pattern` | m05-type-driven | wrapper, type safety |
| `PhantomData ` | m05-type-driven | marker, lifetime |
| `type state pattern` | m05-type-driven | state machine, compile-time |

### Test Commands

```bash
claude -p "newtype pattern"
claude -p "PhantomData "
```

---

## m09-domain

| Query | Expected Skill | Expected Elements |
|-------|----------------|-------------------|
| `DDD in Rust` | m09-domain | aggregate, entity |
| `domain model ` | m09-domain | value object, repository |
| `aggregate root` | m09-domain | invariant, consistency |

### Test Commands

```bash
claude -p "DDD in Rust"
claude -p
```

---

## m10-performance

| Query | Expected Skill | Expected Elements |
|-------|----------------|-------------------|
| `benchmark ` | m10-performance | criterion, bench |
| `criterion ` | m10-performance | black_box, throughput |
| ` zero copy` | m10-performance | Cow, bytes |

### Test Commands

```bash
claude -p "Rust "
claude -p "benchmark "
```

---

## m11-ecosystem

| Query | Expected Skill | Expected Elements |
|-------|----------------|-------------------|
| ` crate` | m11-ecosystem | crates.io, popularity |
| `Cargo.toml ` | m11-ecosystem | version, workspace |
| `feature flags ` | m11-ecosystem | optional, cfg |

### Test Commands

```bash
claude -p "crate"
claude -p "feature flags "
```

---

## m12-lifecycle

| Query | Expected Skill | Expected Elements |
|-------|----------------|-------------------|
| `RAII pattern` | m12-lifecycle | Drop, scope |
| `Drop trait ` | m12-lifecycle | destructor, cleanup |
| `scopeguard ` | m12-lifecycle | defer, guard |

### Test Commands

```bash
claude -p "RAII pattern"
claude -p "Drop trait "
```

---

## m13-domain-error

| Query | Expected Skill | Expected Elements |
|-------|----------------|-------------------|
| `retry ` | m13-domain-error | backoff, exponential |
| `circuit breaker ` | m13-domain-error | state, threshold |

### Test Commands

```bash
claude -p "retry "
claude -p "circuit breaker "
```

---

## m14-mental-model

| Query | Expected Skill | Expected Elements |
|-------|----------------|-------------------|
| ` Rust` | m14-mental-model | ownership, mindset |
| ` Java Rust` | m14-mental-model | comparison, transition |

### Test Commands

```bash
claude -p "Rust"
claude -p "Rust "
```

---

## m15-anti-pattern

| Query | Expected Skill | Expected Elements |
|-------|----------------|-------------------|
| `code smell Rust` | m15-anti-pattern | refactor, improve |
| `Rust ` | m15-anti-pattern | avoid, better |
| `clone ` | m15-anti-pattern | unnecessary, performance |

### Test Commands

```bash
claude -p "Rust "
claude -p "clone "
```

---

## Validation Checklist

- [ ] All Layer 2 skills trigger correctly
- [ ] Design-related queries route properly
- [ ] Chinese keywords work
- [ ] No conflicts with Layer 1 skills
