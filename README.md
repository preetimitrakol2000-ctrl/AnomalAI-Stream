# AnomalAI-Stream

AnomalAI-Stream is a native Python implementation of isolation-based anomaly detection tailored for high-velocity streaming data (like smart grid or traffic telemetry). By avoiding heavy frameworks, this engine calculates isolation anomalies using pure mathematical vector routing.

## 🛠️ Architecture & Features
* **Zero-Dependency Core:** Implemented using foundational Python algorithms to minimize memory footprints.
* **Sliding-Window Processing:** Evaluates data variance across dynamic temporal arrays.
* **Hackathon Use-case:** Ideal for edge computing environments where installing heavy AI libraries is impossible.

## 📦 Execution
```bash
python stream.py
