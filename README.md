# AIoT Energy Forecasting Toolkit  
![License](https://img.shields.io/badge/License-MIT%20with%20Citation%20Clause-blue)

**Modeling AI-Driven IoT Energy Consumption: From Device-Level Forecasts to System-Level Dynamics**  
📄 SpliTech 2025 — Milovan Medojevic, Nikola Markovic, Aleksandar Rikalovic

---

##  Overview

This repository implements a dual-framework energy forecasting toolkit designed for AI-enabled IoT (AIoT) systems. It captures both **device-level energy usage** and **system-wide workload dynamics** using complementary modeling approaches:

- 📈 **Bottom-Up Model** — Aggregates power draw across heterogeneous AIoT device classes.
- 📉 **Top-Down Model** — Projects total energy from global inference workloads and efficiency trends.
- 🤖 **Agent-Based Model** — Simulates dynamic workloads, device interactions, and energy consumption over networks.

Together, these models enable researchers and policymakers to evaluate energy trends, optimize deployments, and explore sustainability constraints for AI at the edge.



##  Motivation

AI workloads are rapidly shifting to the network edge — with over 2 billion edge AI devices projected by 2025. This raises critical energy implications for sustainability, infrastructure, and environmental impact.

 📊 Forecasts estimate AIoT energy consumption reaching **112–131 TWh/year** by 2025 — ~0.4–0.45% of global electricity production.


##  Features

✅ Analytical models: exponential + logistic growth

✅ Dual modeling: device-level vs workload-level energy forecasting

✅ Sensitivity analysis for growth rate and efficiency

✅ Parameterized simulation inputs for 2025 AIoT baseline

✅ Agent-based modeling engine with customizable dynamics




## 🛠️ Installation

```bash
git clone https://github.com/your-username/aiot-energy-forecasting.git
cd aiot-energy-forecasting
pip install -r requirements.txt
```

## 📂 Repository Structure

```
├── application.py             # Main forecasting logic
├── tutorial.ipynb             # Interactive tutorial
├── docs/
│   ├── overview.md            # Background & AIoT context
│   ├── models.md              # Analytical model details
│   ├── agent_based_model.md   # Simulation framework
│   └── parameters.md          # Key variables & equations
├── data/                      # Sample input datasets
└── README.md
```

##  Quick Start

Run both forecasting models with default parameters:

```bash
python application.py
```

Or launch the interactive Jupyter tutorial:

```bash
jupyter notebook tutorial.ipynb
```

## Documentation

* [`docs/overview.md`](docs/overview.md) — Contextual motivation & scope
* [`docs/models.md`](docs/models.md) — Forecasting equations and logic
* [`docs/agent_based_model.md`](docs/agent_based_model.md) — ABM system design
* [`docs/parameters.md`](docs/parameters.md) — All variables and default values

## Citation

Please cite our SpliTech 2025 paper if you use this toolkit in your work:

```bibtex
@inproceedings{medojevic2025aiot,
  title={Modeling AI-Driven IoT Energy Consumption: From Device-Level Forecasts to System-Level Dynamics},
  author={Medojevic, Milovan and Markovic, Nikola and Rikalovic, Aleksandar},
  booktitle={SpliTech 2025},
  year={2025}
}
```

## 📄 License

MIT License


