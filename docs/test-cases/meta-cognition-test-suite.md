# Meta-Cognition


---


```

fn calculate_fee(amount: f64, rate: f64) -> f64 {
    amount * rate
}

fn main() {
    let amount = 0.1 + 0.2;
    let fee = calculate_fee(amount, 0.03);
    println!("Fee: {}", fee); // 0.009000000000000001 0.009
}

```


|------|------|------|


```
Layer 1: → IEEE 754
    ↑
Layer 3: →
    ↓
Layer 2: rust_decimal::Decimal
```


```rust
use rust_decimal::Decimal;
use rust_decimal_macros::dec;

fn calculate_fee(amount: Decimal, rate: Decimal) -> Decimal {
    amount * rate
}

fn main() {
    let amount = dec!(0.1) + dec!(0.2); // 0.3
    let fee = calculate_fee(amount, dec!(0.03));
    println!("Fee: {}", fee); // 0.009
}
```

---


```
Web API

use std::rc::Rc;

struct AppConfig {
    db_url: String,
    api_key: String,
}

async fn handle_request(config: Rc<AppConfig>) {
}

#[tokio::main]
async fn main() {
    let config = Rc::new(AppConfig {
        db_url: "postgres://...".into(),
        api_key: "secret".into(),
    });

    tokio::spawn(handle_request(config.clone())); //
}

: `Rc<AppConfig>` cannot be sent between threads safely
```


|------|------|------|


```
Layer 1: Rc Send →
    ↑
Layer 3: Web →
    ↓
Layer 2:
    - OnceLock<AppConfig> ()
    - lazy_static! ()
    - Arc<AppConfig> ()
```


```rust
use std::sync::OnceLock;

static CONFIG: OnceLock<AppConfig> = OnceLock::new();

fn get_config() -> &'static AppConfig {
    CONFIG.get_or_init(|| AppConfig {
        db_url: std::env::var("DATABASE_URL").unwrap(),
        api_key: std::env::var("API_KEY").unwrap(),
    })
}

async fn handle_request() {
    let config = get_config(); // clone
}
```

---


```
CLI panic

fn process_file(path: &str) -> String {
    let content = std::fs::read_to_string(path).unwrap();
    let config: Config = serde_json::from_str(&content).unwrap();
    config.name.to_uppercase()
}

```


|------|------|------|


```
Layer 1: unwrap() panic →
    ↑
Layer 3: CLI → exit code
    ↓
Layer 2: CLI
    - anyhow::Result
    - main() -> Result<(), anyhow::Error>
    - miette
```


```rust
use anyhow::{Context, Result};

fn process_file(path: &str) -> Result<String> {
    let content = std::fs::read_to_string(path)
        .with_context(|| format!(": {}", path))?;

    let config: Config = serde_json::from_str(&content)
        .with_context(|| format!(": {}", path))?;

    Ok(config.name.to_uppercase())
}

fn main() -> Result<()> {
    let result = process_file("config.json")?;
    println!("{}", result);
    Ok(())
}

// miette
```

---


```
API

async fn upload_handler(data: Vec<u8>) -> Result<String, Error> {
    let compressed = compress(&data); // CPU

    let hash = sha256(&compressed); // CPU

    storage.save(&hash, &compressed).await?;

    Ok(hash)
}

```


|------|------|------|


```
Layer 1: async → tokio worker
    ↑
Layer 3: Web →
    ↓
Layer 2:
    - CPU → spawn_blocking rayon
    - I/O → async
```


```rust
async fn upload_handler(data: Vec<u8>) -> Result<String, Error> {
    // CPU
    let (compressed, hash) = tokio::task::spawn_blocking(move || {
        let compressed = compress(&data);
        let hash = sha256(&compressed);
        (compressed, hash)
    }).await?;

    storage.save(&hash, &compressed).await?;

    Ok(hash)
}
```

---


### 1. Claude


### 2. rust-skills Claude

- (Layer 1 → 3 → 2)


|------|----------|------------|
| crate |  | ✅ () |

---


```

let amount = 0.1 + 0.2;
let fee = amount * 0.03;
println!("Fee: {}", fee); // 0.009000000000000001

```

- : "round() "
- : "f64rust_decimal"
