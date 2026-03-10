# Skill

> Claude Code Skills


Claude Code Skills
- skill `description`
- "" skill
- skill


|------|----------|----------|----------|
|B: Hook| | |plugin|
|C: CLAUDE.md| | | |

---


****: skills`~/.claude/skills/`


```
~/.claude/skills/
├── _shared/ #
│ ├── rust-defaults.md # Rust
│ └── python-defaults.md # Python
│
├── tokio/
│   ├── SKILL.md
│   └── references/
│       └── rust-defaults.md → ../../_shared/rust-defaults.md
│
├── tokio-task/
│   ├── SKILL.md
│   └── references/
│       └── rust-defaults.md → ../../_shared/rust-defaults.md
│
└── serde/
    ├── SKILL.md
    └── references/
        └── rust-defaults.md → ../../_shared/rust-defaults.md
```


```bash
mkdir -p ~/.claude/skills/_shared

cat > ~/.claude/skills/_shared/rust-defaults.md << 'EOF'
# Rust Code Generation Defaults

## Cargo.toml
- edition = "2024" (NOT 2021)
- Use latest stable crate versions

## Code Style
- Prefer explicit error handling over .unwrap()
- Use anyhow/thiserror for errors
EOF

# 3. skill
for skill in tokio tokio-task tokio-sync serde axum; do
    mkdir -p ~/.claude/skills/$skill/references
    ln -sf ../../_shared/rust-defaults.md ~/.claude/skills/$skill/references/rust-defaults.md
done
```

### SKILL.md

```markdown
## Code Generation Rules

**IMPORTANT: Before generating code, read `./references/rust-defaults.md`**

Key rules (see rust-defaults.md for full list):
- Use edition = "2024"
- Use latest crate versions
```


|------|------|

---

## B: Hook

****: pluginrust-skills


`UserPromptSubmit` hook

```
→ Hook → → Claude
```


```
my-plugin/
├── .claude/
│ ├── settings.json # Hook
│   └── hooks/
│ └── inject-rules.sh #
└── skills/
```


**.claude/settings.json**:
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "(?i)(rust|cargo|tokio|async|await)",
        "command": ".claude/hooks/inject-rules.sh"
      }
    ]
  }
}
```

**.claude/hooks/inject-rules.sh**:
```bash
#!/bin/bash
cat << 'EOF'

=== CODE GENERATION RULES ===

When generating Rust code:
- Use edition = "2024" in Cargo.toml
- Use latest stable crate versions
- Prefer explicit error handling

===

EOF
```


|------|------|

---

## C: CLAUDE.md


```
~/.claude/CLAUDE.md #
```


```markdown
# Global Claude Code Rules

## Rust Defaults
- Use edition = "2024"
- Use latest crate versions

## Python Defaults
- Use Python 3.12+
- Use type hints
```


|------|------|

---


****: skills


SKILL.md

```markdown
# tokio/SKILL.md

## Code Generation Rules
- Use edition = "2024"
- Use latest crate versions

# tokio-task/SKILL.md

## Code Generation Rules
- Use edition = "2024" #
- Use latest crate versions #
```


|------|------|

---


```
┌─────────────────────────────────────────────────────────┐
└─────────────────────────────────────────────────────────┘

    │
    │
    └── → plugin skill
                      │
                      ├── Plugin → Hook (B)
                      │
                      └── skill → (D)
```

---


### 1: tokio skills

```bash
~/.claude/skills/
├── _shared/rust-defaults.md
├── tokio/references/rust-defaults.md → ...
├── tokio-task/references/rust-defaults.md → ...
└── tokio-sync/references/rust-defaults.md → ...
```

### 2: rust-skills

```bash
rust-skills/
├── .claude/hooks/rust-skill-eval-hook.sh # edition 2024
└── skills/m01-ownership/SKILL.md #
```


```bash
~/.claude/CLAUDE.md #
```

---


```bash
#!/bin/bash
# setup-skill-inheritance.sh

SHARED_DIR="$HOME/.claude/skills/_shared"
SHARED_FILE="rust-defaults.md"

mkdir -p "$SHARED_DIR"

# skills
for skill in "$@"; do
    skill_dir="$HOME/.claude/skills/$skill"
    if [ -d "$skill_dir" ]; then
        mkdir -p "$skill_dir/references"
        ln -sf "../../_shared/$SHARED_FILE" "$skill_dir/references/$SHARED_FILE"
        echo "✓ $skill"
    else
        echo "✗ $skill (not found)"
    fi
done
```

```bash
./setup-skill-inheritance.sh tokio tokio-task tokio-sync serde axum
```

---


|----------|----------|
|skills|**** ( A)|
|plugin|**Hook ** ( B)|
|skill|**** ( D)|
