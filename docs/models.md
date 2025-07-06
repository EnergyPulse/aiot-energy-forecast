# Forecasting Models

This document outlines the mathematical models used to estimate AIoT energy consumption. The framework integrates both device-level and system-wide perspectives to support accurate and scalable forecasting.

---

## 📊 Bottom-Up Device-Level Model

This model estimates total energy consumption by summing contributions from different device classes:

### Equation (7):

```math
E_t^{hw} = \sum_{j=1}^n N_{j,t} \cdot P_j \cdot \Delta t
```

Where:

- \(N_{j,t}\): number of active devices of class \(j\) at time \(t\)
- \(P_j\): average power draw (watts) of device class \(j\)
- \(\Delta t\): time interval in hours (typically 8760 hours/year)

### Overhead Function:

Real-world deployments incur additional energy overhead from data movement, memory, and cooling:

```math
f(D_t, M_t) = \alpha D_t^\gamma + \beta M_t^\delta
```

or

```math
f(D_t, M_t) = \eta D_t^\gamma M_t^\delta
```

Where \(D_t\) is data volume and \(M_t\) is number of inference tasks.

### Device Growth:

- **Exponential Growth**:

```math
N_{j,t} = N_{j,0}(1 + r_{Nj})^t
```

- **Logistic Growth**:

```math
N_{j,t} = \frac{K_j}{1 + A_j e^{-r_{Nj} t}}, \quad A_j = \frac{K_j}{N_{j,0}} - 1
```

---

## ⚙️ Top-Down Workload-Level Model

This model expresses total energy as the product of workload size and energy per unit inference:

### Equation (14):

```math
E(t) = N(t) \cdot e(t)
```

Where:

- \(N(t)\): number of inferences
- \(e(t)\): energy per inference (Wh)

### Exponential Formulation:

```math
N(t) = N_0 e^{r_N t}, \quad e(t) = e_0 e^{-\rho t}
```

```math
E_{exp}(t) = N_0 e_0 e^{(r_N - \rho)t}
```

### Logistic Workload Forecast:

```math
N(t) = \frac{K}{1 + A e^{-r_N t}}, \quad E_{log}(t) = \frac{K e_0 e^{-\rho t}}{1 + A e^{-r_N t}}
```

---

## 📉 Sensitivity Analysis

Forecasts are highly sensitive to small errors in growth or efficiency rates:

### Equation (19):

```math
\frac{\partial E}{\partial r_N} = t E, \quad \frac{\partial E}{\partial \rho} = -t E
```

This implies a 1% error in \(r_N\) causes \~\(t\)% error in \(E(t)\).

### Uncertainty Propagation:

Assuming \(r_N, \rho\) are normal with std. dev \(\sigma_r, \sigma_\rho\):

```math
E_{95\%}(t) = E_{exp}(t) \cdot \exp(\pm 1.96t \sqrt{\sigma_r^2 + \sigma_\rho^2})
```

---

## 📈 Visualization



*Figure: Energy forecasts under exponential vs logistic growth. Efficiency gains (**\(\rho\)**) modulate total demand over time.*

---

## 🧠 Insights

- If \(r_N < \rho\): energy use **declines** over time
- If \(r_N = \rho\): energy **plateaus**
- If \(r_N > \rho\): energy use **grows exponentially**

By tuning efficiency \(\rho\) and capping device counts \(K_j\), sustainable trajectories can be achieved.

---

