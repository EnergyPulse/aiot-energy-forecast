# Agent-Based Model

This document outlines the agent-based simulation framework for modeling spatiotemporal energy consumption dynamics in distributed AIoT systems.

---

## 🤖 Agent Classes

### 1. IoT Device Agents (i = 1, ..., N)

Each represents a computational unit (e.g., MCU, CPU, NPU).

#### State Variables:

- `s_i(t) ∈ {0, 1}` — Active or idle
- `u_i(t) ∈ [0, 1]` — Utilization level
- `b_i(t)` — Optional energy buffer (e.g., battery/harvesting)

### 2. Workload Source Agents (k = 1, ..., K)

Generate inference or training jobs.

- `λ_k(t)` — Arrival rate (e.g., Poisson-distributed)

---

## 🔗 Interaction Topology

Agents are connected via a graph \(G = (V, E)\), defined by an adjacency matrix \(A_{ij}\). Edges represent:

- Proximity
- Communication capability
- Offloading feasibility

The topology governs:

- Task routing
- Collaborative processing
- Load balancing

---

## 🔄 Dynamics

### Task Assignment:

Tasks are assigned based on routing probabilities:

```math
m_i(t) \sim \text{Binomial} \left( \sum_k \lambda_k(t), P(i|k, t) \right)
```

### Activation State:

```math
P(s_i(t+1) = 1) = 1 - e^{-\kappa m_i(t)}
```

Where \(\kappa\) controls how quickly devices become active based on load.

### Utilization:

```math
u_i(t+1) = \frac{m_i(t)}{C_j(i)}
```

\(C_j\) is the capacity of hardware class \(j\).

### Power Consumption:

```math
P_i(t) = P_j^{\text{idle}} + (P_j^{\text{peak}} - P_j^{\text{idle}}) u_i(t)
```

---

## 🔥 Overhead Energy Model

Total system energy includes nonlinear overheads:

```math
E_{\text{overhead}}(t) = \alpha \sum_i u_i(t)^\gamma + \beta |\{i : s_i = 1\}|^\delta
```

- \(\gamma\), \(\delta\) ≥ 1: scale nonlinearly with load and active population

---

## 🌱 Population Growth

Devices evolve over time:

```math
N(t+1) = N(t) + r_N N(t)\left(1 - \frac{N(t)}{K}\right)
```

---

## 🧠 Learning Policies

Routing policies \(P(i|k,t)\) adapt using reinforcement learning to minimize system-wide energy. Reward = negative total energy consumption.

---

## 📈 Visualization



*Figure: Example simulation showing dynamic energy use and device activation over time.*

---

## 🧪 Calibration & Validation

The model is calibrated using:

- Historical IoT workload traces
- Real-world energy measurements

Validation is performed by comparing simulation output to known energy profiles using error metrics (e.g., RMSE, MAPE).

---

## 💡 Use Cases

- Regional energy footprint modeling
- Demand response simulations
- Federated learning energy impact
- Real-time adaptive workload dispatch

---

