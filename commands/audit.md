# /audit

Heavy-weight security and safety audit using os-checker tools.

## Usage

```
/audit [mode]
```

## Parameters

- `mode` (optional): Audit mode
  - `security` - (default)
  - `safety` - unsafe
  - `concurrency` -
  - `full` -

## When to Use

|------|------|
| **unsafe ** | `/audit safety` |

## Audit Modes

### Security (Default)


|------|----------|
| `cargo audit` | CVE |
| `geiger` | unsafe |

```bash
cargo audit
cargo geiger
```

### Safety

unsafe

|------|----------|
| `miri` | Undefined Behavior |
| `rudra` |  |
| `geiger` | unsafe |

```bash
cargo +nightly miri test
# rudra
```

****: nightly toolchain

### Concurrency


|------|----------|
| `lockbud` |  |
| `atomvchecker` |  |

### Full


## Integration with os-checker Skills

skills

| Skill |  |
|-------|------|
| `os-checker-checkers` |  |
| `os-checker-cli` | os-checker |
| `os-checker-diagnostics` |  |
| `os-checker-setup` |  |

## Issue Prioritization

|--------|----------|------|
| Critical | `Miri`, `Rudra`, `Audit`, `Cargo` |  |
| High | `Lockbud(Probably)`, `Semver Violation` |  |
| Medium | `Lockbud(Possibly)`, `Atomvchecker` |  |
| Low | `Geiger`, `Outdated` |  |

## Example Output

```
Security Audit Report
═══════════════════════════════════════════

[1/2] cargo audit
  ✗ 2 vulnerabilities found

  CRITICAL:
    RUSTSEC-2024-0001: Memory corruption in foo v1.2.3
    → Upgrade to foo v1.2.4

  HIGH:
    RUSTSEC-2024-0002: DoS vulnerability in bar v2.0.0
    → Upgrade to bar v2.0.1

[2/2] cargo geiger
  Unsafe usage in dependencies:
    ├── libc: 127 unsafe blocks
    ├── tokio: 45 unsafe blocks
    └── your-crate: 3 unsafe blocks

═══════════════════════════════════════════
Recommended Actions:
1. Update foo to v1.2.4 (CRITICAL)
2. Update bar to v2.0.1 (HIGH)
3. Review unsafe usage with /unsafe-check
```

## Tool Installation

```bash
# Security
cargo install cargo-audit

# Safety (needs nightly)
rustup +nightly component add miri

# Geiger
cargo install cargo-geiger

# Full os-checker suite
cargo install os-checker
```

## Batch Audit (Multiple Repos)

os-checker

```bash
cat > audit-config.json << 'EOF'
{
  "org/repo1": {},
  "org/repo2": {},
  "org/repo3": {}
}
EOF

os-checker run --config audit-config.json --emit results.json
```

## Related Commands

- `/rust-review` - (clippy)
- `/unsafe-check` - unsafe
- `/unsafe-review` - unsafe
