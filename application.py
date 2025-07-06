#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AIoT Energy Consumption Forecaster
Copyright (c) 2024 [Your Name/Organization]

This implementation is based on:
Medojevic, M., Markovic, N., & Rikalovic, A. (2025). 
"Modeling AI-Driven IoT Energy Consumption: From Device-Level 
Forecasts to System-Level Dynamics"

Licensed under MIT License with Academic Citation Requirement
"""

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Core computation function
def compute_values(params):
    N0_bu, rN_bu, K_bu, P_avg, Dt, overhead_pct, \
    N0_td, e0, rN_td, rho, K_td, A_td, \
    sigma_r, sigma_rho, start_year, end_year = params

    years = np.arange(start_year, end_year + 1)
    t_vec = years - start_year

    # Bottom-Up Calculations
    N_bu_exp = N0_bu * np.power((1 + rN_bu), t_vec)
    E_bu_exp = N_bu_exp * P_avg * Dt * (1 + overhead_pct)
    A_bu = (K_bu / N0_bu) - 1
    N_bu_log = K_bu / (1 + A_bu * np.exp(-rN_bu * t_vec))
    E_bu_log = N_bu_log * P_avg * Dt * (1 + overhead_pct)

    # Top-Down Calculations
    E_td_exp = N0_td * e0 * np.exp((rN_td - rho) * t_vec)
    E_td_log = (K_td * e0 * np.exp(-rho * t_vec)) / (1 + A_td * np.exp(-rN_td * t_vec))

    # Sensitivity Analysis
    dE_drN = t_vec * E_td_exp
    dE_drho = -t_vec * E_td_exp

    # Confidence Intervals
    ci_factor = np.exp(1.96 * t_vec * np.sqrt(sigma_r**2 + sigma_rho**2))
    E_td_lower = E_td_exp / ci_factor
    E_td_upper = E_td_exp * ci_factor

    return {
        "years": years,
        "E_bu_exp": E_bu_exp,
        "E_bu_log": E_bu_log,
        "E_td_exp": E_td_exp,
        "E_td_log": E_td_log,
        "E_td_lower": E_td_lower,
        "E_td_upper": E_td_upper,
        "dE_drN": dE_drN,
        "dE_drho": dE_drho
    }

# App Configuration
st.set_page_config(
    page_title="AIoT Energy Forecaster",
    layout="wide",
    page_icon="🔌"
)

# Academic Attribution
st.sidebar.markdown("""
### Research Basis
Implements models from:  
**Medojevic et al. (2025)**  
*Modeling AI-Driven IoT Energy Consumption*  

**License**:  
[MIT] - Free for use with citation
""")

# Main Interface
st.title("🔌 AIoT Energy Forecast Tool")
st.markdown("""
Forecast energy consumption using:
- **Bottom-Up** (device populations)
- **Top-Down** (workload metrics)  
*Reference: Medojevic et al. (2025)*
""")

# Parameter Inputs with Tooltips
with st.sidebar.expander("Bottom-Up Parameters"):
    N0_bu = st.number_input(
        "Initial Devices (N₀)", 
        value=2e9, 
        format="%e",
        help="Baseline number of AIoT devices in the starting year"
    )
    rN_bu = st.slider(
        "Growth Rate r_N", 
        0.0, 0.5, 0.15, step=0.01,
        help="Annual growth rate of device population"
    )
    K_bu = st.number_input(
        "Saturation K", 
        value=5e9, 
        format="%e",
        help="Maximum possible number of devices (carrying capacity)"
    )
    P_avg = st.number_input(
        "Avg Power (W)", 
        value=7.5,
        help="Average power consumption per active device"
    )
    Dt = st.number_input(
        "Hours per Year", 
        value=8760,
        help="Annual operational hours per device (8760 = 24/7 operation)"
    )
    overhead_pct = st.slider(
        "Overhead %", 
        0, 50, 10,
        help="Additional energy for cooling, networking, etc."
    ) / 100

with st.sidebar.expander("Top-Down Parameters"):
    daily_inf = 1000
    N0_td = st.number_input(
        "Annual Inferences", 
        value=2e9 * daily_inf * 365, 
        format="%e",
        help="Total inference operations per year across all devices"
    )
    e0 = st.number_input(
        "Energy per Inference (Wh)", 
        value=0.000154, 
        format="%f",
        help="Base energy consumption per AI inference operation"
    )
    rN_td = st.slider(
        "Inference Growth Rate", 
        0.0, 0.5, 0.15, step=0.01,
        help="Annual increase in total inference workload"
    )
    rho = st.slider(
        "Efficiency Gain ρ", 
        0.0, 0.5, 0.30, step=0.01,
        help="Annual improvement in energy efficiency per inference"
    )
    K_td = st.number_input(
        "Workload Saturation", 
        value=1e16, 
        format="%e",
        help="Maximum sustainable inference workload"
    )

with st.sidebar.expander("Uncertainty Parameters"):
    sigma_r = st.slider(
        "σ_r (Growth Uncertainty)", 
        0.0, 0.2, 0.05, step=0.01,
        help="Standard deviation in growth rate estimates"
    )
    sigma_rho = st.slider(
        "σ_ρ (Efficiency Uncertainty)", 
        0.0, 0.2, 0.05, step=0.01,
        help="Standard deviation in efficiency improvement estimates"
    )

with st.sidebar.expander("Time Range"):
    start_year = st.number_input(
        "Start Year", 
        value=2024, 
        step=1,
        help="Baseline year for projections"
    )
    end_year = st.number_input(
        "End Year", 
        value=2035, 
        step=1,
        help="Final projection year"
    )

# Calculations
A_td = (K_td / N0_td) - 1
params = (
    N0_bu, rN_bu, K_bu, P_avg, Dt, overhead_pct,
    N0_td, e0, rN_td, rho, K_td, A_td,
    sigma_r, sigma_rho, start_year, end_year
)
results = compute_values(params)
years = results["years"]

# Visualizations
tab1, tab2, tab3 = st.tabs(["Forecast Comparison", "Sensitivity Analysis", "Confidence Intervals"])

with tab1:
    st.subheader("Model Comparison")
    forecast_df = pd.DataFrame({
        "Year": np.tile(years, 4),
        "Energy (TWh)": np.concatenate([
            results["E_bu_exp"] / 1e12,
            results["E_bu_log"] / 1e12,
            results["E_td_exp"] / 1e12,
            results["E_td_log"] / 1e12
        ]),
        "Model": ["BU Exp"]*len(years) + ["BU Log"]*len(years) + 
                ["TD Exp"]*len(years) + ["TD Log"]*len(years)
    })
    
    chart = alt.Chart(forecast_df).mark_line().encode(
        x="Year:O",
        y="Energy (TWh)",
        color="Model"
    ).properties(height=500)
    st.altair_chart(chart, use_container_width=True)

with tab2:
    st.subheader("Parameter Sensitivity (Top-Down Exponential Model)")
    sens_df = pd.DataFrame({
        "Year": years,
        "∂E/∂r_N": results["dE_drN"] / 1e12,
        "∂E/∂ρ": results["dE_drho"] / 1e12
    })
    st.line_chart(sens_df.set_index("Year"))

with tab3:
    st.subheader("95% Confidence Intervals (Top-Down Exponential Model)")
    ci_df = pd.DataFrame({
        "Year": years,
        "Lower Bound": results["E_td_lower"] / 1e12,
        "Upper Bound": results["E_td_upper"] / 1e12,
        "Expected": results["E_td_exp"] / 1e12
    })
    st.area_chart(ci_df.set_index("Year"))

# Data Export
st.subheader("Raw Output Data")
with st.expander("View Complete Data Table"):
    full_df = pd.DataFrame({
        "Year": years,
        "BU_Exp (TWh)": results["E_bu_exp"] / 1e12,
        "BU_Log (TWh)": results["E_bu_log"] / 1e12,
        "TD_Exp (TWh)": results["E_td_exp"] / 1e12,
        "TD_Log (TWh)": results["E_td_log"] / 1e12,
        "TD_Lower (TWh)": results["E_td_lower"] / 1e12,
        "TD_Upper (TWh)": results["E_td_upper"] / 1e12,
        "Sens_rN (TWh)": results["dE_drN"] / 1e12,
        "Sens_rho (TWh)": results["dE_drho"] / 1e12
    })
    
    # Format numbers for display
    styled_df = full_df.style.format({
        "BU_Exp (TWh)": "{:.3f}",
        "BU_Log (TWh)": "{:.3f}",
        "TD_Exp (TWh)": "{:.3f}",
        "TD_Log (TWh)": "{:.3f}",
        "TD_Lower (TWh)": "{:.3f}",
        "TD_Upper (TWh)": "{:.3f}",
        "Sens_rN (TWh)": "{:.3f}",
        "Sens_rho (TWh)": "{:.3f}"
    })
    
    st.dataframe(styled_df)
    
    # CSV download
    csv = full_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        "Download CSV",
        csv,
        "aiot_energy_forecast.csv",
        "text/csv",
        help="Download full dataset as CSV for further analysis"
    )

# Academic Footer
st.markdown("---")
st.caption("""
**Academic Use**: When publishing results from this tool, please cite:  
*Medojevic, M., Markovic, N., & Rikalovic, A. (2025). Modeling AI-Driven IoT Energy Consumption: From Device-Level Forecasts to System-Level Dynamics*  
Code provided under [MIT License](https://opensource.org/licenses/MIT)
""")