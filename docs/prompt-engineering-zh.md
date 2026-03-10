# Prompt

> Prompt


```
: token

: "Rc cannot be sent"
: P("Arc") > P("...")

```


```

: P("Arc") = 0.7, P("") = 0.3
: P("Arc") = 0.2, P("") = 0.8

```

---


|------|--------|------|----------|


```markdown
CRITICAL: You MUST load both L1 and L3 skills.
NEVER skip the domain constraint analysis.
This is MANDATORY and NON-NEGOTIABLE.

IMPORTANT: Always include the reasoning chain.
You are REQUIRED to reference domain rules.

You should trace through all layers.
It is recommended to provide code examples.

You can include additional context.
You may reference related skills.

Optionally, mention performance implications.
```

---


### 1. CRITICAL + MUST

```markdown
CRITICAL: You MUST follow the meta-cognition framework.

- CRITICAL
- MUST
```


```markdown
DO:
- Load both L1 and L3 skills
- Output reasoning chain
- Reference domain constraints

DON'T:
- Skip domain analysis
- Output only "use Arc"
- Ignore the context

```


```markdown
CORRECT Response:
```
### Reasoning Chain
+-- Layer 1: Send/Sync Error
+-- Layer 3: Web Domain constraint
+-- Layer 2: Design decision
```

WRONG Response:
```
Use Arc instead of Rc.
```

```


```markdown
**IF** domain keywords are present,
**THEN** you MUST load BOTH L1 and L3 skills.

**IF** error code detected,
**THEN** start from Layer 1 and trace UP.

```


```markdown
## STEP 1: IDENTIFY (MANDATORY)
...

## STEP 2: LOAD SKILLS (MANDATORY)
...

## STEP 3: OUTPUT (MANDATORY)
...

: + MANDATORY
```

---


```markdown
should do this →
SHOULD do this →
You SHOULD do this →
You MUST do this →
CRITICAL: You MUST... →
```


```markdown
## STEP 1: IDENTIFY LAYER

### Layer 1 Signals:
- Error codes: E0382, E0597
- Keywords: borrow, lifetime

### Layer 3 Signals:
- Domain keywords: Web API, HTTP

---

First identify the layer. Look for error codes like E0382
or keywords like borrow. Also check for domain keywords...
```


```markdown
| Keywords | Action |
|----------|--------|
| Web API, HTTP | Load domain-web |
| payment | Load domain-fintech |

If you see Web API or HTTP, load domain-web.
If you see payment, load domain-fintech.
```

---


|---|------|------|
| `MUST` | | You MUST include... |
| `NEVER` | | NEVER skip... |
| `ALWAYS` | | ALWAYS check... |
| `REQUIRED` | | This is REQUIRED |
| `MANDATORY` | | MANDATORY step |
| `NON-NEGOTIABLE` | | This is NON-NEGOTIABLE |


|---|------|------|
| `NEVER` | | NEVER output only... |
| `DO NOT` | | DO NOT skip... |
| `AVOID` | | AVOID generic answers |
| `FORBIDDEN` | | This is FORBIDDEN |
| `NOT ACCEPTABLE` | | Partial compliance is NOT ACCEPTABLE |


|---|------|------|
| `IF...THEN` |...| IF domain detected, THEN load... |
| `WHEN` | | WHEN error code present... |
| `UNLESS` | | UNLESS explicitly asked... |
| `ONLY IF` | | ONLY IF user requests... |


|---|------|------|
| `CRITICAL` | | CRITICAL: This is essential |
| `IMPORTANT` | | IMPORTANT: Note that... |
| `NOTE` | | NOTE: This affects... |
| `WARNING` | | WARNING: Do not... |

---

## rust-skills

### Hook

```bash
=== MANDATORY: META-COGNITION ROUTING ===

CRITICAL: You MUST follow the COMPLETE meta-cognition framework.
Partial compliance (only loading L1 skill) is NOT ACCEPTABLE.

# 2. CRITICAL + MUST
```

### Skill Description

```yaml
description: "CRITICAL: Use for ALL Rust questions. Triggers on: ..."

# 1. CRITICAL
# 3. Triggers on:
```


```markdown
## STEP 3: MANDATORY OUTPUT FORMAT

Your response MUST include ALL of these sections:

### Reasoning Chain
```
+-- Layer 1: [specific error]
|       ^
+-- Layer 3: [domain constraint]
|       v
+-- Layer 2: [design decision]
```

# 1. MANDATORY + ALL
```


```markdown
CORRECT Response:
```
### Reasoning Chain
+-- Layer 1: Send/Sync Error
...
```

WRONG Response (stops at L1):
```
Problem: Rc is not Send
Solution: Use Arc
```

# 2. (stops at L1)
```

---


```markdown
You should probably include the reasoning chain.
It would be nice to reference domain constraints.

You MUST include the reasoning chain.
CRITICAL: Reference domain constraints.
```


```markdown
Follow the meta-cognition framework.

STEP 1: Identify entry layer (L1/L2/L3)
STEP 2: Load appropriate skills using Skill() tool
STEP 3: Trace through layers (UP or DOWN)
STEP 4: Output with reasoning chain format
```


```markdown
Output should include reasoning chain.

Output MUST include reasoning chain:
```
### Reasoning Chain
+-- Layer 1: [error]
+-- Layer 3: [constraint]
+-- Layer 2: [decision]
```
```


```markdown
Include domain analysis.

Include domain analysis.

WRONG (without domain analysis):
  "Use Arc instead of Rc"

CORRECT (with domain analysis):
  "From domain-web: handlers run on any thread,
   therefore Arc + State extractor is recommended"
```

---


```
   "Web API Rc cannot be sent"


```


```
□ Skills?
```

---


|------|----------|


```markdown
1. (CRITICAL/IMPORTANT)
2. (You MUST...)
3. (CORRECT:)
4. (WRONG:)
5. (IF...THEN...)
```


```markdown
```


```

- → CRITICAL/MUST
```

---


1. ****: should < IMPORTANT < CRITICAL + MUST
2. ****: CORRECT vs WRONG
4. ****: IF...THEN
