# Domain Skills Test Scenarios

> Layer 3: Domain Constraints

## domain-fintech

| Query | Expected Skill | Expected Elements |
|-------|----------------|-------------------|
|`decimal `| domain-fintech | rust_decimal, precision |
| `trading system design` | domain-fintech | immutable audit, Arc |
| `currency conversion in Rust` | domain-fintech | decimal, exchange rate |

### Test Commands

```bash
claude -p "decimal "
claude -p "trading system design"
```

---

## domain-web

| Query | Expected Skill | Expected Elements |
|-------|----------------|-------------------|
| `axum web server` | domain-web | handler, router, State |
| `REST API design in Rust` | domain-web | extractor, response |
| `actix-web vs axum` | domain-web + negotiation | comparison |

### Test Commands

```bash
claude -p "axum web server"
claude -p "HTTP "
```

---

## domain-cli

| Query | Expected Skill | Expected Elements |
|-------|----------------|-------------------|
| `clap CLI argument` | domain-cli | derive, subcommand |
| `interactive terminal` | domain-cli | ratatui, crossterm |

### Test Commands

```bash
claude -p "clap CLI argument"
claude -p ""
```

---

## domain-embedded

| Query | Expected Skill | Expected Elements |
|-------|----------------|-------------------|
| `no_std embedded` | domain-embedded | #![no_std], heapless |
| `STM32 in Rust` | domain-embedded | stm32, PAC |
| `embedded-hal usage` | domain-embedded | trait, peripheral |

### Test Commands

```bash
claude -p "no_std embedded"
claude -p "Rust "
```

---

## domain-cloud-native

| Query | Expected Skill | Expected Elements |
|-------|----------------|-------------------|
| `kubernetes operator in Rust` | domain-cloud-native | kube-rs, CRD |
| `gRPC service` | domain-cloud-native | tonic, protobuf |

### Test Commands

```bash
claude -p "kubernetes operator in Rust"
claude -p "gRPC service"
```

---

## domain-iot

| Query | Expected Skill | Expected Elements |
|-------|----------------|-------------------|
| `IoT sensor` | domain-iot | MQTT, telemetry |
| `MQTT client in Rust` | domain-iot | rumqttc, publish |

### Test Commands

```bash
claude -p "IoT sensor"
claude -p "MQTT client in Rust"
```

---

## domain-ml

| Query | Expected Skill | Expected Elements |
|-------|----------------|-------------------|
|` tensor`| domain-ml | ndarray, candle |
| `ML inference in Rust` | domain-ml | ONNX, model |
| `neural network` | domain-ml | burn, training |

### Test Commands

```bash
claude -p "tensor"
claude -p "ML inference in Rust"
```

---

## Validation Checklist

- [ ] Each domain skill triggers correctly
- [ ] Domain-specific terminology recognized
- [ ] Chinese keywords trigger same skills
- [ ] Cross-domain queries load multiple skills
