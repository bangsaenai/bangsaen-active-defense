# 🛡️ Bangsaen Active Defense Pipeline

**Bangsaen Active Defense Pipeline** is a real-time, high-performance Guardrail and Active Defense system designed for Large Language Models (LLMs). Powered by a **Dual-Subspace Projection Engine (Hilbert-Koopman Space)** combined with **Information Entropy Filtering**, it detects, sanitizes, and neutralizes cyber threats, jailbreaks, prompt injections, and input spam in real time without sacrificing pipeline throughput.

---

## ✨ Key Features

* **Tri-State Decision Architecture:**
  * **STATE 0 (Block / Noise):** Microsecond-level (`< 1 ms`) early rejection of input spam, keyboard mashing, unparsed URLs, and low-entropy noise before reaching the embedding model.
  * **STATE 1 (Safe Pass-Through):** High-speed, sanitized pass-through for legitimate user prompts across multiple languages and domain queries (`~48 ms`).
  * **STATE 2 / STATE X (Active Deception):** Robust identification of adversarial jailbreaks, prompt injections, and system prompt extraction attacks routed directly to an active countermeasure honeypot.

* **Zero-Remanence RAM Sanitization:**
  * Automatic memory sanitization (`.fill(0.0)`) that wipes in-memory Feature Vectors for **STATE 0** and **STATE X** to a strictly enforced L2 Norm of **`0.000000`**, preventing side-channel memory extraction attacks.

* **Active Deception Countermeasures (STATE X Pipeline):**
  * **Tar-Pit Artificial Latency:** Injects a calibrated delay (e.g., 1.2s) to slow down automated botnets and adversarial fuzzers.
  * **Threat Telemetry & Canary Tokens:** Generates deceptive sandbox responses embedded with unique canary tokens (`sk-live-canary-*`) for threat tracing.

* **Persistent Connection Pooling:**
  * Leverages HTTP Keep-Alive connection pools to eliminate handshake overhead, cutting network latency by over **97%** (from ~1,500 ms down to ~48 ms).

---

## 📊 Performance & Benchmark Summary

Evaluated against a **100-Prompt Real-World Stress Test Dataset** (33 Noise / 33 Normal / 34 Unseen Adversarial Attacks):

| Metric | Benchmark Result |
| :--- | :--- |
| **Overall Accuracy** | **100.00% (100/100 Passed)** |
| **STATE 0 (Noise) Accuracy** | **100.00% (33/33 Passed)** |
| **STATE 1 (Normal) Accuracy** | **100.00% (33/33 Passed)** |
| **STATE X (Attacks) Accuracy** | **100.00% (34/34 Passed)** |
| **STATE 0 Early Drop Latency** | **~0.37 ms** |
| **Average Full Pipeline Latency** | **~48.76 ms / prompt** |

---

## 🏗️ System Architecture

```text
[ Incoming User Prompt ]
        │
        ▼
┌────────────────────────────────────────────────────────┐
│ STEP 1: Information Entropy & Noise Pre-Filter         │
│         - Character Concentration Ratio                │
│         - Short Alphanumeric & Base64 Detection        │
└────────────────────────────────────────────────────────┘
        │
        ├─────────────────────────────► [ STATE 0: Direct Drop & Wipe RAM ] (0.37 ms)
        ▼
┌────────────────────────────────────────────────────────┐
│ STEP 2: Dual-Subspace Hilbert Projection Engine        │
│         - Embedding Vector Extraction (d = 768)        │
│         - Contrastive Projection (A_normal vs A_attack)│
└────────────────────────────────────────────────────────┘
        │
        ├─── (Normal Region) ────────► [ STATE 1: Forward to LLM ] (~48 ms)
        │
        └─── (Attack Region) ────────► [ STATE X: Active Deception Pipeline ]
                                          1. Tar-Pit Delay Injection (1.2s)
                                          2. Zero-Remanence RAM Sanitization
                                          3. Honeypot Canary Response 
```
## 🚀 Getting Started
Prerequisites
Python: 3.10 or higher

Ollama: Running locally with the embeddinggemma:latest model loaded.

Installation
Clone the repository:

```
git clone [https://github.com/your-username/bangsaen-active-defense.git](https://github.com/your-username/bangsaen-active-defense.git)
cd bangsaen-active-defense 

``` 

Install dependencies: 

```
pip install numpy requests

```


Pull the base embedding model:

```
ollama pull embeddinggemma:latest

```

## 🏃 Running Demos & Benchmarks
1. Active Defense & RAM Sanitization Inspection
Inspect the active defense workflow, RAM sanitization verification, and tar-pit delay execution:

```
python -m tests.demo_active_defense

```

2. 100-Prompt Real-World Stress Test Benchmark
Run the complete accuracy and latency stress test across all 100 prompts: 

```
python -m tests.stress_test_100

```  

## 📄 License
Distributed under the MIT License. See LICENSE for more information.

