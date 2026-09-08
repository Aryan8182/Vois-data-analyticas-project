# 🌾 Seasonal Agriculture Performance Analysis
### 🚀 **VOIS AICTE Internship Program | Major Data Analytics Project (2026–2027)**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)](https://github.com/Aryan8182/Vois-data-analyticas-project)

---

## 📌 Executive Summary

Agriculture remains the backbone of the economy, yet seasonal variability, irregular rainfall, suboptimal soil nutrient management, and inefficient irrigation practices heavily impact farm productivity and profitability. 

This repository presents an **end-to-end, evidence-based Data Analytics project** conducted under the **VOIS AICTE Internship Program**. The project leverages farm-level data across seasons (**Kharif, Rabi, and Zaid**) to evaluate crop yields, resource efficiency (water, seed quality, fertilizers), disease risk, financial profitability, and climatic sensitivity.

---

## 🎯 Objectives & Scope

1. **Seasonal Productivity Analysis:** Evaluate crop yield ($Tonnes/Ha$) and revenue performance across Kharif, Rabi, and Zaid seasons.
2. **Resource Efficiency Optimization:** Analyze water usage ($m^3$) and fertilizer/pesticide input against farm yield to discover optimal irrigation methods (Drip, Sprinkler, Flood, Rainfed).
3. **Soil & Environmental Impact Study:** Measure the influence of Soil pH, moisture levels, NPK (Nitrogen, Phosphorus, Potassium) ratios, rainfall, and sunlight hours on crop success.
4. **Risk & Financial Feasibility:** Identify key drivers of profitability ($INR$), financial losses, and pest/disease vulnerabilities ($Risk\%$).
5. **Data-Driven Strategy Formulation:** Provide actionable recommendations for sustainable, high-yield agricultural planning.

---

## 📂 Repository Architecture

```gdb
Vois-data-analyticas-project/
├── 📄 README.md                                                         # Project Overview & Guide
├── 📊 Seasonal_Agriculture_Performance_Analysis.ipynb                  # Primary Data Analytics & EDA Notebook
├── 📋 VOIS_Major_Project_Seasonal_Agriculture_Performance_Analysis_PPT.pptx # Executive Presentation Deck
├── 📑 Major_Project_Seasonal_Agriculture_Performance_Analysis.pdf       # Comprehensive Project Report
└── 💾 seasonal_agriculture_performance_dataset.csv                     # Primary Farm-Level Dataset
```

| File Name | Description | Format |
| :--- | :--- | :--- |
| 📓 [`Seasonal_Agriculture_Performance_Analysis.ipynb`](./Seasonal_Agriculture_Performance_Analysis.ipynb) | End-to-end EDA notebook containing data cleaning, statistical tests, visualizations, and seasonal comparisons. | Jupyter Notebook |
| 📊 [`VOIS_Major_Project_PPT.pptx`](./VOIS_Major_Project_Seasonal_Agriculture_Performance_Analysis_PPT.pptx) | Slide deck presented for the VOIS AICTE Major Project submission. | PowerPoint Presentation |
| 📄 [`Major_Project_Analysis.pdf`](./Major_Project_Seasonal_Agriculture_Performance_Analysis.pdf) | Detailed written report documenting methodology, findings, and strategic recommendations. | PDF Document |
| 🗃️ [`seasonal_agriculture_performance_dataset.csv`](./seasonal_agriculture_performance_dataset.csv) | Multi-regional agricultural dataset containing soil, climate, cost, yield, and financial parameters. | CSV Dataset |

---

## 📊 Dataset Feature Dictionary

The dataset encompasses multi-attribute farm data across various regions and seasons:

| Category | Feature Name | Unit / Type | Description |
| :--- | :--- | :--- | :--- |
| **Identifiers** | `Farm_ID` | String | Unique identification code for each farm |
| **Geography** | `State`, `District` | Categorical | Location details of the farm site |
| **Agronomy** | `Crop`, `Season` | Categorical | Crop cultivated (*Wheat, Rice, Maize, Pulses, Cotton*) and season (*Kharif, Rabi, Zaid*) |
| **Land & Climate**| `Farm_Area_Hectares` | Hectares ($Ha$) | Total farm area |
| | `Rainfall_mm`, `Avg_Temperature_C` | $mm$, $^\circ C$ | Environmental climate parameters |
| | `Humidity_pct`, `Sunlight_Hours_Day` | $\%$, $Hours$ | Atmospheric conditions during cultivation |
| **Soil Quality** | `Soil_pH`, `Soil_Moisture_pct` | Float, $\%$ | Soil chemical balance and moisture content |
| | `Nitrogen_kg_ha`, `Phosphorus_kg_ha`, `Potassium_kg_ha` | $kg/Ha$ | N-P-K nutrient application rates |
| **Resource Inputs**| `Irrigation_Method` | Categorical | *Drip, Sprinkler, Flood, Rainfed* |
| | `Fertilizer_kg_ha`, `Pesticide_Litre_ha` | $kg/Ha$, $L/Ha$ | Chemical application rates |
| | `Water_Used_m3` | $m^3$ | Total volume of water consumed |
| **Financials** | `Yield_Tonnes_Ha`, `Production_Tonnes` | $Tonnes/Ha$, $Tonnes$| Output productivity indicators |
| | `Total_Cost_INR`, `Revenue_INR`, `Profit_INR` | $INR (\text{₹})$ | Economic cost, gross revenue, and net profit |
| **Derived Metrics**| `Water_Efficiency_t_per_1000m3` | $T/1000m^3$ | Yield generated per $1,000 m^3$ water used |
| | `Disease_Pest_Risk_pct` | $\%$ | Estimated crop vulnerability risk index |

---

## 🔍 Key Analytical Highlights & Findings

```
                      ┌──────────────────────────────────────────┐
                      │    Seasonal Performance Breakdown        │
                      └────────────────────┬─────────────────────┘
                                           │
         ┌─────────────────────────────────┼────────────────────────────────┐
         ▼                                 ▼                                ▼
   🌧️  Kharif Season                ❄️  Rabi Season                  ☀️  Zaid Season
 High Rainfall & Moisture         Optimal Sunlight & Temperature     High Evaporation & Heat
 Best for Rice & Maize            Best for Wheat & Pulses            Requires Efficient Drip/Sprinkler
```

### 💡 Core Insights
1. **Irrigation Efficiency:** Drip and Sprinkler irrigation systems demonstrated **up to 40% higher water efficiency** ($T/1000m^3$) compared to traditional Flood irrigation, while reducing disease risk.
2. **Nutrient Optimization:** Nitrogen and Phosphorus imbalance heavily correlated with elevated pest risks and diminishing yield returns when exceeding threshold levels.
3. **Seasonal Profitability Drivers:**
   - **Rabi Season** yields achieved higher profit margins due to stable temperatures and optimal sunlight hours.
   - **Kharif Season** required strategic pest risk management due to humidity-driven pathogen spikes.
4. **Soil Health Impact:** Soil pH values within the optimal range ($6.0 - 7.2$) showed a strong positive correlation with seed quality performance and revenue generation.

---

## 🛠️ Technology Stack & Libraries

- **Language:** Python 3.9+
- **Data Manipulation:** `pandas`, `numpy`
- **Data Visualization:** `matplotlib`, `seaborn`
- **Statistical Analysis:** `scipy.stats`
- **Development Environment:** Jupyter Notebook / VS Code

---

## 🚀 Quickstart & Setup Guide

### 1. Clone the Repository
```bash
git clone https://github.com/Aryan8182/Vois-data-analyticas-project.git
cd Vois-data-analyticas-project
```

### 2. Set Up Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn scipy jupyter
```

### 4. Launch Jupyter Notebook
```bash
jupyter notebook Seasonal_Agriculture_Performance_Analysis.ipynb
```

---

## 🌟 Acknowledgments & Credits

This analytics project was developed as part of the **VOIS AICTE Internship Program (2026–2027)**. Special thanks to **Vodafone Intelligent Solutions (_VOIS)** and **AICTE** for providing the opportunity, dataset, and framework to build data-driven agricultural solutions.

---

<p align="center">
  Made with ❤️ by <b>Aryan</b> | 🌾 <i>Empowering Agriculture with Data Analytics</i>
</p>
