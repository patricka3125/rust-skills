# /rust-review

Lightweight Rust code review using clippy.

## Usage

```
/rust-review [path]
```

## Parameters

- `path` (optional): Path to file or directory to review. Defaults to current directory.

## What It Does

`cargo clippy`

|----------|------|
| `clippy::correctness` | |
| `clippy::suspicious` | |
| `clippy::complexity` | |
| `clippy::perf` | |
| `clippy::style` | |

## Workflow

2. **clippy** - `cargo clippy --message-format=json`

## Example Output

```
Rust Code Review: src/lib.rs

Running clippy...

═══════════════════════════════════════════
Results: 3 issues found
═══════════════════════════════════════════

ERROR (1):
  src/lib.rs:42 [clippy::unwrap_used]
    → unwrap() called on Result
    → Fix: Use ? operator or handle error explicitly

WARNING (2):
  src/lib.rs:15 [clippy::needless_clone]
    → Clone is not needed here
    → Fix: Remove .clone()

  src/lib.rs:28 [clippy::manual_map]
    → Use Option::map instead of match
    → Fix: x.map(|v| v + 1)

═══════════════════════════════════════════
```

## Clippy Configuration

`clippy.toml` `Cargo.toml` clippy

```toml
# Cargo.toml
[lints.clippy]
unwrap_used = "deny"
expect_used = "warn"
```

## NOT Included

**** `/rust-review`

|------|------|----------|
| `cargo fmt` | | |
| `miri` |nightly| `/audit safety` |
| `cargo audit` | | `/audit security` |
| `lockbud` | | `/audit concurrency` |

## Related Commands

- `/audit` - os-checker
- `/unsafe-check` - unsafe
- `/guideline` -
