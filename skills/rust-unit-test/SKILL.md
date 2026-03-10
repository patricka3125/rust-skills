---
name: rust-unit-test
description: "Use for Rust unit testing best practices. Triggers: test, unit test, assert, assertion, claims, nextest, cargo-nextest, tokio::test, async test, test runner, test setup, fixture, parameterized test, mock, #[test], #[cfg(test)], test module, pretty_assertions, rstest, mockall, test organization, test patterns, flaky test, test coverage"
user-invocable: false
---

# Rust Unit Testing

> **Layer 2: Design Choices**

## Core Question

**What am I testing, and what's the right level of confidence for this code?**

Before writing a test:
- Is this logic that the **type system** can't enforce?
- Is this an **expected behavior** or a **regression guard**?
- Is this **sync** or **async** code?

---

## Error → Design Question

| Error | Don't Just Say | Ask Instead |
|-------|----------------|-------------|
| Test passes locally, fails in CI | "Add retry" | Is the test relying on ordering or shared state? |
| Flaky async test | "Use `sleep`" | Is the test awaiting properly or racing? |
| Test is slow | "Mark it `#[ignore]`" | Should this be an integration test instead? |
| Too many mocks | "Add more mocks" | Is the code too tightly coupled? |

---

## Thinking Prompt

Before writing tests:

1. **What layer am I testing?**
   - Pure logic → unit test (no async, no I/O)
   - Async I/O → `#[tokio::test]`
   - Integration glue → `tests/` directory

2. **What assertion style fits?**
   - Equality → `assert_eq!` / `pretty_assertions`
   - Variant checking → `claims` macros
   - Multiple checks → `assert2::check!`
   - Parameterized → `rstest`

3. **How should I run these tests?**
   - Local dev → `cargo nextest run`
   - CI → `cargo nextest run --profile ci`

---

## Recommended Crate Stack

### `Cargo.toml` Setup

```toml
[dev-dependencies]
claims = "0.8"               # Result/Option/Poll assertions
pretty_assertions = "1.4"    # Colorful diff output on assert_eq failure
rstest = "0.25"              # Fixtures + parameterized tests
tokio = { version = "1", features = ["macros", "rt", "rt-multi-thread", "test-util"] }
mockall = "0.13"             # Trait-based mocking
```

### Nextest Config (`.config/nextest.toml`)

```toml
[profile.default]
# Mark tests slow after 30s, kill after 120s
slow-timeout = { period = "30s", terminate-after = 4 }

[profile.ci]
# Don't stop on first failure in CI
fail-fast = false
# Retry flaky tests up to 2 times
retries = 2
```

---

## Tool Reference

### 1. `claims` — Expressive Assertions for Rust Types

`claims` provides assertion macros that std is missing, especially for
`Result`, `Option`, and `Poll`. Every macro also has a `debug_*` counterpart
that is only active in debug builds.

| Category | Macros | Use When |
|----------|--------|----------|
| **Comparison** | `assert_ge!`, `assert_gt!`, `assert_le!`, `assert_lt!` | Numeric bounds, ordering checks |
| **Result** | `assert_ok!`, `assert_err!`, `assert_ok_eq!`, `assert_err_eq!` | Validating `Result` variant and inner value |
| **Option** | `assert_some!`, `assert_none!`, `assert_some_eq!` | Validating `Option` variant and inner value |
| **Poll** | `assert_pending!`, `assert_ready!`, `assert_ready_ok!`, `assert_ready_err!`, `assert_ready_eq!` | Testing futures / polling |
| **Matching** | `assert_matches!` | Pattern matching assertions |

#### Examples

```rust
use claims::{assert_ok, assert_err, assert_some_eq, assert_gt};

#[test]
fn parse_valid_config() {
    let result = Config::from_str("key=value");
    let config = assert_ok!(result); // Unwraps + asserts Ok
    assert_some_eq!(config.get("key"), "value");
}

#[test]
fn reject_negative_port() {
    let result = parse_port("-1");
    assert_err!(result);
}

#[test]
fn buffer_respects_capacity() {
    let buf = RingBuffer::new(16);
    assert_gt!(buf.capacity(), 0);
}
```

**Why `claims` over manual matching:**

```rust
// Without claims — verbose, unclear on failure
let result = parse("input");
assert!(result.is_ok());
assert_eq!(result.unwrap(), expected); // panics if Err

// With claims — one step, great error messages
assert_ok_eq!(parse("input"), expected);
```

---

### 2. `cargo-nextest` — Modern Test Runner

Nextest runs each test in its own **process**, providing:
- **Isolation**: No shared state between tests, no ordering issues.
- **Parallelism**: Tests run concurrently across CPU cores by default.
- **Slow test detection**: Tests exceeding a threshold are flagged `SLOW`.
- **Retries**: Flaky tests can be retried with configurable backoff.
- **Better output**: Clean, structured pass/fail display with timing.

#### Common Commands

| Command | Purpose |
|---------|---------|
| `cargo nextest run` | Run all tests |
| `cargo nextest run -p my-crate` | Run tests for a specific package |
| `cargo nextest run test_name` | Run tests matching a name |
| `cargo nextest run --profile ci` | Run with CI profile (no fail-fast) |
| `cargo nextest run -j4` | Run with 4 parallel test processes |
| `cargo nextest run --run-ignored=only` | Run only `#[ignore]`d tests |
| `cargo nextest list` | List all tests without running them |

#### Key Differences from `cargo test`

| Feature | `cargo test` | `cargo nextest` |
|---------|--------------|-----------------|
| Isolation | Tests share a process | Each test runs in its own process |
| Parallelism | Thread-level | Process-level (better isolation) |
| Fail-fast | Not default | Default (configurable) |
| Slow detection | None | Built-in with configurable thresholds |
| Retries | None | Built-in with backoff strategies |
| Output | Verbose | Structured, concise |
| Doc tests | Supported | **Not supported** (use `cargo test --doc`) |

> **Note**: Nextest does **not** run doc tests. Run `cargo test --doc` separately.

---

### 3. `#[tokio::test]` — Async Test Runtime

Use `#[tokio::test]` instead of `#[test]` for any test that needs `.await`.
By default, each test gets its own **current-thread** runtime.

#### Runtime Flavors

```rust
// Default: current-thread (single-threaded, deterministic)
#[tokio::test]
async fn test_single_thread() {
    let result = my_async_fn().await;
    assert_eq!(result, 42);
}

// Multi-thread: realistic but less deterministic
#[tokio::test(flavor = "multi_thread", worker_threads = 2)]
async fn test_multi_thread() {
    let result = my_async_fn().await;
    assert_eq!(result, 42);
}
```

#### Time Control with `start_paused`

The `start_paused = true` option (requires `test-util` feature) freezes
the runtime clock at the start, so `tokio::time::sleep` and timeouts
resolve **instantly** when the runtime has no other work. This makes
time-dependent tests deterministic and fast.

```rust
#[tokio::test(start_paused = true)]
async fn test_timeout_logic() {
    // This completes instantly — no real waiting!
    tokio::time::sleep(Duration::from_secs(60)).await;
    assert!(true, "60 seconds passed instantly");
}

#[tokio::test(start_paused = true)]
async fn test_retry_backoff() {
    let start = tokio::time::Instant::now();
    retry_with_backoff(|| async { Err("fail") }, 3).await;
    // Verify total elapsed time matches expected backoff
    assert_ge!(start.elapsed(), Duration::from_secs(7));
}
```

#### Common Async Test Pitfalls

| Pitfall | Why Bad | Fix |
|---------|---------|-----|
| `std::thread::sleep` in async test | Blocks the executor | `tokio::time::sleep` |
| Holding `MutexGuard` across `.await` | Deadlocks, blocks other tasks | Scope the lock tightly |
| No timeout on test | Hangs forever on failure | Use `tokio::time::timeout` or nextest `slow-timeout` |
| `tokio::spawn` without `.await`ing | Test passes before task finishes | `handle.await.unwrap()` |
| Non-deterministic timing | Flaky tests | Use `start_paused = true` |

#### Pattern: Testing Channels

```rust
use tokio::sync::mpsc;

#[tokio::test]
async fn test_worker_sends_results() {
    let (tx, mut rx) = mpsc::channel(10);

    tokio::spawn(async move {
        tx.send("done".to_string()).await.unwrap();
    });

    let result = tokio::time::timeout(
        Duration::from_secs(1),
        rx.recv(),
    ).await;

    assert_ok!(result);
    assert_some_eq!(result.unwrap(), "done".to_string());
}
```

#### Pattern: Testing with `JoinSet`

```rust
use tokio::task::JoinSet;

#[tokio::test]
async fn test_parallel_tasks() {
    let mut set = JoinSet::new();
    for i in 0..5 {
        set.spawn(async move { i * 2 });
    }

    let mut results = Vec::new();
    while let Some(res) = set.join_next().await {
        results.push(assert_ok!(res));
    }
    results.sort();
    assert_eq!(results, vec![0, 2, 4, 6, 8]);
}
```

---

### 4. Complementary Tools

#### `pretty_assertions` — Better Diff Output

Drop-in replacement for `assert_eq!` / `assert_ne!` with color-coded diffs.
Essential for comparing large structs, JSON, or multiline strings.

```rust
use pretty_assertions::{assert_eq, assert_ne};

#[test]
fn test_serialization() {
    let output = serialize(&my_struct);
    assert_eq!(output, expected_json); // colored diff on failure
}
```

#### `rstest` — Fixtures & Parameterized Tests

Eliminates boilerplate setup code and generates individual test cases.

```rust
use rstest::{rstest, fixture};

#[fixture]
fn db() -> TestDb {
    TestDb::new_in_memory()
}

#[rstest]
#[case("admin", true)]
#[case("guest", false)]
#[case("", false)]
fn test_user_permissions(db: TestDb, #[case] role: &str, #[case] can_edit: bool) {
    let user = db.create_user(role);
    assert_eq!(user.can_edit(), can_edit);
}
```

#### `mockall` — Trait-Based Mocking

Mock any trait for isolated unit tests. Define the trait, then `#[automock]`.

```rust
use mockall::{automock, predicate::*};

#[automock]
trait EmailSender {
    fn send(&self, to: &str, body: &str) -> Result<(), String>;
}

#[test]
fn test_registration_sends_email() {
    let mut mock = MockEmailSender::new();
    mock.expect_send()
        .with(eq("user@test.com"), always())
        .times(1)
        .returning(|_, _| Ok(()));

    let service = RegistrationService::new(mock);
    assert_ok!(service.register("user@test.com"));
}
```

#### `assert2` — Alternative: Non-Short-Circuiting Checks

The `check!` macro logs all failures without stopping the test early.
Useful when a single test validates multiple independent properties.

```rust
use assert2::{check, assert2};

#[test]
fn test_config_defaults() {
    let config = Config::default();
    check!(config.port == 8080);      // continues even if this fails
    check!(config.host == "0.0.0.0"); // reports all failures at once
    check!(config.workers > 0);
}
```

---

## Decision Flowchart

```
What am I testing?
├─ Pure logic → #[test] + claims/assert_eq
├─ Async logic → #[tokio::test] + claims
├─ Time-dependent → #[tokio::test(start_paused = true)]
└─ External system → mockall + trait abstraction

Repeated setup?
├─ Yes → rstest fixtures (#[fixture])
└─ No → inline setup

Multiple input combinations?
├─ Yes → rstest #[case] or matrix
└─ No → single test

Comparing large/complex output?
├─ Yes → pretty_assertions
└─ No → std assert_eq!

Running tests?
├─ Local → cargo nextest run
├─ CI → cargo nextest run --profile ci
└─ Doc tests → cargo test --doc
```

---

## Anti-Patterns

| Anti-Pattern | Why Bad | Better |
|--------------|---------|--------|
| `#[ignore]` without reason | Hidden tech debt | Fix or delete the test |
| `thread::sleep` in tests | Slow, flaky | `tokio::time::sleep` + `start_paused` |
| Testing private impl details | Brittle to refactoring | Test via public API |
| No assertions (test only "runs") | False confidence | Assert expected outcomes |
| Copy-paste test setup | Unmaintainable | `rstest` fixtures |
| Giant test functions | Hard to debug failure | One logical assertion per test |
| Mocking everything | Tests prove nothing | Mock only external boundaries |

---

## Test Organization Best Practices

```
src/
├── lib.rs
├── parser.rs          # Source file
│   └── mod tests {    # Unit tests (private access)
│       use super::*;
│       use claims::*;
│       use pretty_assertions::assert_eq;
│   }
tests/
├── integration_test.rs  # Integration tests (public API only)
└── common/
    └── mod.rs           # Shared test helpers
```

| Guideline | Rationale |
|-----------|-----------|
| Unit tests in the same file | Access to private functions, easy to find |
| Integration tests in `tests/` | Treat your crate as an external consumer |
| Shared helpers in `tests/common/mod.rs` | Avoid duplication across integration tests |
| `#[cfg(test)]` on test modules | Don't compile test code into the binary |
| Name tests descriptively | `test_parse_rejects_empty_input` > `test1` |

---

## Quick Reference

| Task | Tool |
|------|------|
| Assert `Result` is `Ok`/`Err` | `claims::assert_ok!` / `assert_err!` |
| Assert `Option` is `Some`/`None` | `claims::assert_some!` / `assert_none!` |
| Compare with colored diff | `pretty_assertions::assert_eq!` |
| Parameterized test cases | `rstest` `#[case]` |
| Reusable test setup | `rstest` `#[fixture]` |
| Async test | `#[tokio::test]` |
| Deterministic time in test | `#[tokio::test(start_paused = true)]` |
| Mock a trait | `mockall` `#[automock]` |
| Run tests (local) | `cargo nextest run` |
| Run tests (CI) | `cargo nextest run --profile ci` |
| Run doc tests | `cargo test --doc` |
| List all tests | `cargo nextest list` |

---

## Trace Up ↑

| Situation | Trace To | Question |
|-----------|----------|----------|
| Tests too brittle | m09-domain | Is the public API well-defined? |
| Too many mocks | m09-domain | Is coupling too tight? |
| Async tests flaky | m07-concurrency | Is the concurrency model correct? |
| Error assertions unclear | m06-error-handling | Are error types well-designed? |

## Trace Down ↓

From design to implementation:

```
"Need to test error paths"
    ↓ Use: claims assert_err!, assert_ok_eq!

"Need to test async code"
    ↓ Use: #[tokio::test] + tokio::time

"Need parameterized tests"
    ↓ Use: rstest #[case]

"Need to isolate from I/O"
    ↓ Use: mockall #[automock] on trait boundary
```

---

## Related Skills

| When | See |
|------|-----|
| Concurrency patterns | m07-concurrency |
| Error handling strategy | m06-error-handling |
| Domain design (testability) | m09-domain |
| Performance testing | m10-performance |
| Anti-patterns in tests | m15-anti-pattern |
