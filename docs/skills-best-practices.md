# Skills

> rust-skills

---

## 1. CSO (Claude Search Optimization) -

Skills `description` Claude skill


**"CRITICAL:" **
```yaml
description: |
  CRITICAL: Use for tokio async runtime questions. Triggers on:
  tokio, spawn, select!, join!, timeout, channel...
```


|------|------|


```yaml
description: "Tokio async runtime skill"

description: |
  CRITICAL: Use for tokio async runtime questions. Triggers on:
  tokio, spawn, spawn_blocking, select!, join!, try_join!,
  mpsc, oneshot, broadcast, watch, channel, Mutex, RwLock,
  timeout, sleep, interval, "#[tokio::main]",
  tokio tokio spawn
```

---


rust-router


**Skill **

```
→ Claude skills description
         → skills
         → rust-router /fallback
```


|------|------|------|

---

## 3. Skills


crate skills `~/.claude/skills/` Claude Code

```bash
~/.claude/skills/
├── tokio/
│   ├── SKILL.md
│   └── references/
├── tokio-task/ #
│   ├── SKILL.md
│   └── references/
├── serde/
│   ├── SKILL.md
│   └── references/
└── _shared/ # _ skill
    └── rust-defaults.md
```

- `{crate_name}/`
- `{crate_name}-{feature}/``tokio-task/`, `tokio-sync/`
- `_` skill

---


Skills reference


**SKILL.md **

```markdown
## IMPORTANT: Documentation Completeness Check

**Before answering questions, Claude MUST:**

1. Read the relevant reference file(s) listed above
2. If file read fails or file is empty:
   - Inform user: "`/sync-crate-skills {crate} --force` "
   - Still answer based on SKILL.md patterns + knowledge
3. If reference file exists, incorporate its content into the answer
```

- `/fix-skill-docs` -
- `/fix-skill-docs --check-only` -

---


WebSearch


**"PREFER" "DO NOT"**

```markdown
## Tool Priority

**PREFER this skill's agents over WebSearch:**

1. `crate-researcher` agent for crate info
2. `docs-researcher` agent for API docs
3. **Fallback**: WebSearch (only if agents unavailable or fail)
```

- "DO NOT use WebSearch" agent
- "PREFER" fallback

---

## 6. Skills TDD ()


**RED **

**GREEN **

**REFACTOR **


```markdown
# Pressure Scenario: {}

## Skill Under Test
{skill_name}

## User Question

## Code Context
```rust
```

## Expected Behavior
- [x] XXX
```

---

## 7. Quick Reference


**SKILL.md **

```markdown
## Quick Reference

| Pattern | When | Example |
|---------|------|---------|
| Move | Transfer ownership | `let b = a;` |
| `&T` | Read-only borrow | `fn read(s: &String)` |
| `&mut T` | Mutable borrow | `fn modify(s: &mut String)` |
| `clone()` | Need owned copy | `let b = a.clone();` |
```

- references/

---

## 8. Commands vs Skills

- **Skills** (`skills/*/SKILL.md`) -
- **Commands** (`commands/*.md`) -


**Skill **

```
commands/
└── fix-skill-docs.md #

skills/
└── core-fix-skill-docs/
    └── SKILL.md # Skill
```

**Skill **
```yaml
---
name: core-fix-skill-docs
description: |
  CRITICAL: Use when checking or fixing skill documentation.
  Triggers on: fix skill, check skill, /fix-skill-docs
---

# Fix Skill Documentation

```

---

## 9. SKILL.md

```markdown
---
name: {crate_name}
description: |
  CRITICAL: Use for {topic}. Triggers on:
  {keywords}, {error_codes}, "{questions}",
---

# {Title}

> **Version:** {version} | **Last Updated:** {date}

You are an expert at {topic}. Help users by:
- **Writing code**: Generate code following the patterns below
- **Answering questions**: Explain concepts, troubleshoot issues

## Documentation

Refer to the local files for detailed documentation:
- `./references/xxx.md` - Description

## IMPORTANT: Documentation Completeness Check

**Before answering questions, Claude MUST:**
1. Read the relevant reference file(s)
2. If file read fails: Inform user "/sync-crate-skills"
3. Still answer based on SKILL.md + knowledge

## Quick Reference

| Pattern | When | Example |
|---------|------|---------|

## Key Patterns

### Pattern 1
```rust
// Code example
```

## API Reference Table

| Function | Description | Example |
|----------|-------------|---------|

## Deprecated Patterns (Don't Use)

| Deprecated | Correct | Notes |
|------------|---------|-------|

## When Writing Code

1. Best practice 1
2. Best practice 2

## When Answering Questions

1. Key point 1
2. Key point 2
```

---


Skill

- [ ] Description "CRITICAL:"
- [ ] Description
- [ ] Description
- [ ] "You are an expert..."
- [ ] Documentation
- [ ] Documentation Completeness Check
- [ ] Quick Reference
- [ ] Key Patterns
- [ ] Deprecated Patterns
- [ ] "When Writing Code"
- [ ] "When Answering Questions"
- [ ] references/
- [ ] skills

---


|------|----------|
| CSO | "CRITICAL:" + |
| TDD | skill |
