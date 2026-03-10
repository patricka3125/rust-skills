
> Agent


1. **Skill references **skill
   ```
   ~/.claude/skills/{crate}/references/{item}.md
   ```

2. ****fallback
   ```
   ~/.claude/cache/rust-docs/{source}/{path}.json
   ```


|----------|----------|
| docs.rs crate | `~/.claude/cache/rust-docs/docs.rs/{crate}/{item}.json` |
| std library | `~/.claude/cache/rust-docs/std/{module}/{item}.json` |
| releases.rs | `~/.claude/cache/rust-docs/releases.rs/{version}.json` |
| lib.rs | `~/.claude/cache/rust-docs/lib.rs/{crate}.json` |
| clippy | `~/.claude/cache/rust-docs/clippy/{lint}.json` |


### JSON

```json
{
  "meta": {
    "url": "https://doc.rust-lang.org/std/marker/trait.Send.html",
    "fetched_at": "2025-01-16T23:30:00Z",
    "expires_at": "2025-01-23T23:30:00Z",
    "source": "agent-browser",
    "version": "1"
  },
  "content": {
    "title": "std::marker::Send",
    "signature": "pub unsafe auto trait Send { }",
    "description": "Types that can be transferred across thread boundaries...",
    "sections": {
      "implementors": "...",
      "examples": "..."
    }
  }
}
```

### Markdown references/

```markdown
---
url: https://doc.rust-lang.org/std/marker/trait.Send.html
fetched_at: 2025-01-16T23:30:00Z
expires_at: 2025-01-23T23:30:00Z
source: agent-browser
---

# std::marker::Send

**Signature:**
```rust
pub unsafe auto trait Send { }
```

**Description:**
Types that can be transferred across thread boundaries...
```


|----------|--------------|------|
| std library |30| |
| crate docs (stable) |7| |
| releases.rs | | |
| lib.rs (crate info) |1| |
| clippy lints |14|Rust|

## Agent


```
3. (expires_at < now)
```


```
1. actionbook + agent-browser
3. JSON Markdown
```


```
"Send trait "
"refresh tokio::spawn docs"
```


### /rust-skills:cache-status

```
Rust Docs Cache Status:
- std library: 45 items, 12MB
- docs.rs: 128 items, 34MB
- releases.rs: 15 items, 2MB
- Total: 188 items, 48MB

Expired: 23 items
```

### /rust-skills:cache-clean

```
/rust-skills:cache-clean #
/rust-skills:cache-clean --all #
/rust-skills:cache-clean tokio # crate
```


|------|------|
| `agents/docs-cache.md` | |
| `agents/docs-researcher.md` | |
| `agents/std-docs-researcher.md` | |
| `commands/cache-status.md` | |
| `commands/cache-clean.md` | |
