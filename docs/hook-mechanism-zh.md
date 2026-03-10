# Hook

> Hook Skills


### Hook

```
: "Web API Rc cannot be sent"

Claude :
  → "Arc Rc"
  → Skill
```

****: Skill Claude

### Hook

```
: "Web API Rc cannot be sent"

Hook :
  → "Web API", "Send"
  → Skills
```

****: Rust

---

## Hook


```
┌─────────────────────────────────────────────────────────────┐
│ "Web API Rc cannot be sent" │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 hooks/hooks.json                             │
│                                                              │
│  {                                                           │
│    "hooks": {                                                │
│      "UserPromptSubmit": [{                                  │
│        "matcher": "(?i)(rust|Web API|Send|...)",            │
│        "hooks": [{                                           │
│          "type": "command",                                  │
│          "command": "...rust-skill-eval-hook.sh"            │
│        }]                                                    │
│      }]                                                      │
│    }                                                         │
│  }                                                           │
│                                                              │
│ ! → hook │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│           .claude/hooks/rust-skill-eval-hook.sh             │
│                                                              │
│ - Skills │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ Claude │
│                                                              │
│ 1. + Hook │
│ 2. Skills │
└─────────────────────────────────────────────────────────────┘
```

---


### 1. hooks/hooks.json ()

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "(?i)(rust|cargo|rustc|crate|Cargo\\.toml|E0\\d{3}|ownership|borrow|lifetime|Send|Sync|async|await|Arc|Rc|Mutex|trait|generic|Result|Error|panic|unsafe|FFI|Web API|HTTP|axum|actix||||||||)",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/.claude/hooks/rust-skill-eval-hook.sh"
          }
        ]
      }
    ]
  }
}
```


|------|------|
| `UserPromptSubmit` |Hook :|
| `matcher` | |
| `type: command` |shell|
| `${CLAUDE_PLUGIN_ROOT}` | |

### 2. matcher

```regex
(?i)(
  # Rust
  rust|cargo|rustc|crate|Cargo\.toml|

  E0\d{3}|

  ownership|borrow|lifetime|move|clone|

  Send|Sync|async|await|thread|spawn|

  Arc|Rc|Box|RefCell|Cell|Mutex|

  trait|generic|impl|dyn|

  Result|Error|panic|unwrap|

  # Unsafe
  unsafe|FFI|extern|

  Web API|HTTP|axum|actix|payment|trading|CLI|embedded|


  |||what|how|why
)
```

### 3. rust-skill-eval-hook.sh ()

```bash
#!/bin/bash
cat << 'EOF'

=== MANDATORY: META-COGNITION ROUTING ===

CRITICAL: You MUST follow the COMPLETE meta-cognition framework.

## STEP 1: IDENTIFY ENTRY LAYER + DOMAIN

| Keywords in Question | Domain Skill to Load |
|---------------------|---------------------|
| Web API, HTTP, axum | domain-web |
| payment, trading    | domain-fintech |
| CLI, clap, terminal | domain-cli |

**CRITICAL**: If domain keywords present, load BOTH L1 and L3 skills.

## STEP 2: EXECUTE TRACING (MANDATORY)

L1 Error → Trace UP to L3 → Find constraint → Trace DOWN to solution

## STEP 3: MANDATORY OUTPUT FORMAT

### Reasoning Chain
+-- Layer 1: [error]
|       ^
+-- Layer 3: [domain constraint]
|       v
+-- Layer 2: [design decision]

### Domain Constraints Analysis
[Reference domain skill rules]

### Recommended Solution
[Code following best practices]

EOF
```


|------|------|

---

## Hook

### Claude Code Hook

|Hook| | |
|-----------|----------|------|
| `UserPromptSubmit` | |**** -|
| `PreToolUse` | | |
| `PostToolUse` | | |
| `Stop` | | |

### rust-skills Hook

```json
{
  "UserPromptSubmit": [
    {
      "matcher": "...",
      "hooks": [{ "type": "command", "command": "..." }]
    }
  ]
}
```

**UserPromptSubmit**:
- Claude

---


```
: Rust

├── : rust, cargo, crate, ...
├── : E0xxx ()
├── : ownership, borrow, lifetime, ...
├── : Arc, Rc, Mutex, ...
├── : Web API, HTTP, payment, ...
└── : how, why, ...
```


```
: "Web API Send not satisfied"

  → "Send" → m07-concurrency
  → : "Arc"
  → : Web

  → "Web API" → = domain-web
  → "Send" → = m07-concurrency
  → Skills
  → : Web
```

**Hook **:

```
| Keywords in Question | Domain Skill to Load |
|---------------------|---------------------|
| Web API, HTTP, axum | domain-web |
| payment, trading    | domain-fintech |

**CRITICAL**: If domain keywords present, load BOTH L1 and L3 skills.
```


```
  → Claude "Arc"

  → Reasoning Chain
```

**Hook **:

```markdown
## STEP 3: MANDATORY OUTPUT FORMAT

Your response MUST include ALL of these sections:

### Reasoning Chain
+-- Layer 1: [specific error]
|       ^
+-- Layer 3: [domain constraint]
|       v
+-- Layer 2: [design decision]

### Domain Constraints Analysis
- MUST reference specific rules from domain-xxx skill

### Recommended Solution
- Not just fixing the compile error
```

---


### Hook ()

```
rust-skills/
├── hooks/
│ └── hooks.json ← Hook
├── .claude/
│   └── hooks/
│ └── rust-skill-eval-hook.sh ←
└── .claude-plugin/
    └── plugin.json ← hooks
```

**plugin.json**:
```json
{
  "name": "rust-skills",
  "skills": "./skills/",
  "hooks": "./hooks/hooks.json" ←
}
```

### Hook

```
my-project/
└── .claude/
    ├── hooks/
    │   └── my-hook.sh
    └── settings.json ← hooks
```

### Hook

```
~/.claude/
├── hooks/
│   └── global-hook.sh
└── settings.json ← hooks
```

---


```python
# tests/hook-matcher-test.py
import re

matcher = r"(?i)(rust|cargo|E0\d{3}|ownership|borrow|Send|Sync|Web API|)"

test_cases = [
    "Web API Rc cannot be sent",
    "how to use async",
]

for case in test_cases:
    if re.search(matcher, case):
        print(f"✓ : {case}")
    else:
        print(f"✗ : {case}")
```

### 2. Hook

Claude Code Hook :

```
⏺ <user-prompt-submit-hook>
  [Hook ]
```

- Hook
- plugin.json hooks

### 3. Skill


```
⏺ Skill(rust-router)
  ⎿ Successfully loaded skill

⏺ Skill(m07-concurrency)
  ⎿ Successfully loaded skill

⏺ Skill(domain-web)
  ⎿ Successfully loaded skill
```

---


### Q1: Hook


```
□ hooks/hooks.json
□ plugin.json "hooks": "./hooks/hooks.json"
□ matcher
□ (chmod +x)
```

### Q2: Skill


```
□ Hook
□ Skill skills/
□ SKILL.md name
□ description (CRITICAL: Use for...)
```


```
□ Hook
```

---


```
✓ Rust
✓ (how, why)
```


```
✓ (→ Skill)
```


```
✓ Hook hooks/hooks.json
✓ .claude/hooks/
✓ plugin.json
```

---


### hooks/hooks.json

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "(?i)(rust|cargo|rustc|crate|Cargo\\.toml|E0\\d{3}|ownership|borrow|lifetime|move|clone|Send|Sync|async|await|thread|Arc|Rc|Box|RefCell|Mutex|trait|generic|Result|Error|panic|unsafe|FFI|Web API|HTTP|axum|actix|payment|trading|CLI|clap|embedded|no_std||||||||||how to|why)",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/.claude/hooks/rust-skill-eval-hook.sh"
          }
        ]
      }
    ]
  }
}
```

### .claude/hooks/rust-skill-eval-hook.sh

```bash
#!/bin/bash
cat << 'EOF'

=== MANDATORY: META-COGNITION ROUTING ===

CRITICAL: You MUST follow the COMPLETE meta-cognition framework.
Partial compliance (only loading L1 skill) is NOT acceptable.

## STEP 1: IDENTIFY ENTRY LAYER + DOMAIN

### Layer 3 Domain Detection (MUST load if keywords present):

| Keywords | Domain Skill |
|----------|--------------|
| Web API, HTTP, REST, axum, actix | domain-web |
| payment, trading, fintech, decimal | domain-fintech |
| CLI, clap, terminal | domain-cli |
| embedded, no_std, MCU | domain-embedded |

**CRITICAL**: Load BOTH L1 skill AND L3 domain skill.

## STEP 2: EXECUTE TRACING

L1 Error → Trace UP to L3 → Find constraint → Trace DOWN to L2

## STEP 3: MANDATORY OUTPUT FORMAT

### Reasoning Chain
+-- Layer 1: [error]
|       ^
+-- Layer 3: [domain constraint]
|       v
+-- Layer 2: [design decision]

### Domain Constraints Analysis
[Reference specific rules from domain skill]

### Recommended Solution
[Code following domain best practices]

===================================

EOF
```

### .claude-plugin/plugin.json

```json
{
  "name": "rust-skills",
  "version": "1.0.0",
  "description": "Rust development assistant with meta-cognition",
  "skills": "./skills/",
  "hooks": "./hooks/hooks.json"
}
```

---


|------|---------|---------|
|Skill| | |
