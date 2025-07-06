# Model Parameters Reference

This document summarizes the key variables and parameters used across the Bottom-Up, Top-Down, and Agent-Based energy models.

---

## 🔌 Device-Level Parameters

| Symbol     | Description                                | Units           | Example Value (2025) |
|------------|--------------------------------------------|------------------|-----------------------|
| \( N_{j,t} \) | Number of active devices of class \(j\) at time \(t\) | count           | 2.0 × 10⁹             |
| \( P_j \)     | Power draw of device class \(j\)            | Watts (W)        | 7.5                   |
| \( \Delta t \) | Time window                                | Hours/year       | 8,760                 |
| \( K_j \)     | Maximum deployable devices (carrying cap.)  | count           | 3.0 × 10⁹             |
| \( r_{Nj} \)  | Growth rate of device class \(j\)           | 1/year          | 0.12 – 0.18           |

---

## ⚙️ Workload Parameters

| Symbol     | Description                                | Units           | Example Value |
|------------|--------------------------------------------|------------------|----------------|
| \( N(t) \)   | Total number of inferences                 | count/year       | 7.3 × 10¹⁴     |
| \( e(t) \)   | Energy per inference                       | Wh/inference     | 0.000154       |
| \( \rho \)   | Efficiency improvement rate (Koomey's Law) | 1/year           | 0.30 (30%)     |
| \( r_N \)    | Inference workload growth rate             | 1/year           | 0.12 – 0.20     |
| \( K \)      | Maximum workload capacity                  | count/year       | 1.0 × 10¹⁵     |
| \( A \)      | Logistic workload parameter                | dimensionless    | derived         |

---

## 📉 Overhead and Cost Terms

| Symbol     | Description                                | Units           | Notes                   |
|------------|--------------------------------------------|------------------|-------------------------|
| \( f(D_t, M_t) \) | Overhead energy function               | Wh               | nonlinear data + tasks   |
| \( D_t \)   | Total data processed                      | GB/day            | input-dependent          |
| \( M_t \)   | Number of workload operations             | count/day         | usually ~1,000 per day   |
| \( \alpha, \beta \) | Overhead coefficients              | Wh or scaling     | tunable parameters       |
| \( \gamma, \delta \) | Power-law exponents                | dimensionless      | typically ≥ 1            |

---

## 🤖 Agent-Based Model Parameters

| Symbol       | Description                             | Units         | Example |
|--------------|-----------------------------------------|---------------|---------|
| \( s_i(t) \) | Binary device state (active/idle)        | {0, 1}         | –       |
| \( u_i(t) \) | Utilization ratio                        | [0, 1]         | –       |
| \( b_i(t) \) | Energy buffer (battery or supply)        | Wh             | optional|
| \( \lambda_k(t) \) | Task arrival rate of source \(k\)    | tasks/unit time | Poisson |
| \( P_j^{\text{idle}} \) | Power when idle                   | W               | e.g., 2W |
| \( P_j^{\text{peak}} \) | Max power (fully active)          | W               | e.g., 10W|
| \( \kappa \) | Activation sensitivity                    | 1/tasks         | tunable |
| \( C_j \)    | Device class capacity                    | tasks/unit time | e.g., 100|
| \( r_N \)    | Device growth rate                       | 1/year          | 0.15     |
| \( K \)      | Carrying capacity (logistic cap)         | count           | –       |

---

## 📏 Units Used

- **Wh** = Watt-hour (energy)
- **W** = Watts (power)
- **tasks/inferences** = computational events
- **1/year** = annual rate (growth or improvement)

---

## 📚 Sources

- [SpliTech 2025 paper](../MM_NM_AR_Splitech25_IoTEnergy.pdf)
- MLPerf benchmarks (2024–2025)
- IEA Reports (2023–2025)
- NVIDIA, AMD, and EdgeCortix energy datasheets

---

