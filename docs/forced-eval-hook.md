# Forced Eval Hook

> Claude Code Skills


### Claude

> "Claude is so goal focused that it barrels ahead with what it thinks is the best approach. It doesn't check for tools unless explicitly told to."

Claude **skills**skill description


|------|--------|------|
| description | **~20%** | Claude |
| **Forced Eval Hook** | **~84%** |  |
| LLM Eval Hook | ~80% | API |

## Forced Eval Hook


**** Claude skill

- `MANDATORY` -
- `CRITICAL` -
- `MUST` -
- `DO NOT skip` -


```
┌─────────────────────────────────────────────────────────────┐
│                     User Prompt                              │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              UserPromptSubmit Hook                           │
│                                                              │
│ 1. Regex matcher │
│     (?i)(rust|cargo|E0\d{3,4}|...)                          │
│                                                              │
│ 2. → hook script │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│ Hook Script │
│                                                              │
│  === MANDATORY SKILL EVALUATION ===                         │
│                                                              │
│  CRITICAL: Before proceeding, you MUST:                     │
│  1. EVALUATE each skill against this prompt                 │
│  2. State: "[skill-name]: YES/NO - [reason]"                │
│  3. ACTIVATE matching skills using Skill(name)              │
│  4. Only THEN proceed with response                         │
│                                                              │
│  DO NOT skip this evaluation.                               │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│ Claude │
│                                                              │
│ : Hook + User Prompt │
│                                                              │
│ 1. skill │
│ m01-ownership: YES - E0382 │
│ m02-resource: NO - │
│     ...                                                      │
│ 2. Skill(m01-ownership) │
│ 3. skill │
└─────────────────────────────────────────────────────────────┘
```


```
EVALUATE → ACTIVATE → IMPLEMENT
```

1. **EVALUATE**: skill YES/NO
2. **ACTIVATE**: `Skill(skill-name)` skills
3. **IMPLEMENT**:


### 1. Hook (settings.json)

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "(?i)(rust|cargo|crate|E0\\d{3,4}|...)",
        "command": ".claude/hooks/rust-skill-eval-hook.sh"
      }
    ]
  }
}
```

- `UserPromptSubmit`: prompt
- `matcher`: hook
- `command`:

### 2. Hook Script

```bash
#!/bin/bash
cat << 'EOF'

=== MANDATORY SKILL EVALUATION ===

CRITICAL: Before proceeding with this Rust-related request, you MUST:

1. EVALUATE each available rust-skill against this prompt:

   OWNERSHIP & MEMORY:
   - m01-ownership: ownership, borrow, lifetime, E0382, E0597
   - m02-resource: Box, Rc, Arc, RefCell, smart pointer
   ...

2. For EACH potentially relevant skill, state: "[skill-name]: YES/NO - [brief reason]"

3. ACTIVATE all YES skills using: Skill(skill-name)

4. Only THEN proceed with your response

DO NOT skip this evaluation.
DO NOT proceed without activating relevant skills first.
This is MANDATORY for all Rust-related requests.

===================================

EOF
```


1. ****: MANDATORY, CRITICAL, MUST, DO NOT
2. **skills **: Claude
3. ****: YES/NO

### 3. Matcher

```regex
(?i)(rust|cargo|crate|ownership|borrow|lifetime|async|await|
trait|generic|unsafe|ffi|error|result|option|tokio|serde|axum|
.*|.*skill|create.*skill|.*skill)
```

- crate


Hook Claude


skills Claude


"YES/NO - reason" Claude


"Only THEN proceed" Claude


|------|------|
| token | Hook token |
| Regex |  |


### A: description

```yaml
# SKILL.md
description: "Keywords: ownership, borrow, lifetime..."
```

****: Claude skill descriptions

### B: Hook

```
You might want to check available skills before responding.
```

****: "might want" Claude

### C: Forced Eval Hook ()

```
CRITICAL: You MUST evaluate each skill. DO NOT skip.
```


### D: LLM Eval Hook

LLM skills

****: API


### 1. Hook

```
✅ MUST, CRITICAL, MANDATORY, DO NOT skip
❌ should, might, consider, optionally
```

### 2. Skill

```
✅ - skill-name: keyword1, keyword2, keyword3
❌ skill-name ()
```

### 3. Matcher

```
```


- skill hook
- matcher


- [Scott Spence: Claude Code Skill Auto Activation](https://scottspence.com/posts/claude-code-skill-auto-activation)
- [Scott Spence: Claude Code Skill Auto Activation Follow Up](https://scottspence.com/posts/claude-code-skill-auto-activation-follow-up)
- [Claude Code Hooks Documentation](https://docs.anthropic.com/claude-code/hooks)
