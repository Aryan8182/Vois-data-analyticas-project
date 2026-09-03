# Seasonal Agriculture Performance Analysis
**VOIS AICTE Batch1 2026-2027 Major Project**

## 📌 Project Overview
This repository contains the major project **Seasonal Agriculture Performance Analysis** developed for the VOIS AICTE Batch1 (2026-2027) program. The project analyzes **4,000 farm-level agricultural records** across India to investigate performance variations across **Kharif** (monsoon), **Rabi** (winter), and **Zaid** (summer) seasons.

---

## 📁 Repository Structure
```text
├── data/
│   └── seasonal_agriculture_performance_dataset.csv  # Original Dataset (4,000 rows x 28 features)
├── outputs/
│   └── charts/                                        # Exported High-Resolution EDA Charts (300 DPI)
├── seasonal_agriculture_performance_dataset.csv       # Root Dataset copy
├── seasonal_agriculture_analysis.py                    # Complete Data Analytics Pipeline Script
├── Seasonal_Agriculture_Performance_Analysis.ipynb    # Executed Interactive Jupyter Notebook
└── README.md                                          # Project Documentation
```

---

## 🎯 Objectives & Expected Outcomes
- **Understand Seasonal Dynamics**: Analyze how rainfall, temperature, humidity, and sunlight influence crop yield and profitability.
- **Resource Usage Optimization**: Evaluate water efficiency ($t/1000m^3$) across Flood, Drip, Sprinkler, and Rainfed irrigation.
- **Disease & Pest Risk Management**: Quantify environmental conditions driving high pest vulnerability (>50%).
- **Financial Sustainability**: Identify drivers of net farm profit and highlight operational cost anomalies.

---

## ⚙️ Technologies & Libraries Used
- **Language**: Python 3.11+
- **Data Manipulation**: `pandas`, `numpy`
- **Data Visualization**: `matplotlib`, `seaborn`
- **Environment**: Jupyter Notebook, Anaconda

---

## 📊 Key Insights Summary
1. **Kharif (Monsoon)**: Achieves the highest mean yield (**5.63 Tonnes/Ha**) and average profit (**₹178,914.65**), but faces peak pest risk (**54.47%**) due to high humidity (>71%).
2. **Rabi (Winter)**: Provides stable crop yield (**5.09 Tonnes/Ha**) with cool temperatures (23.49°C) and reduced pest vulnerability (**40.48%**).
3. **Zaid (Summer)**: Thermal stress (>31°C) and water scarcity result in average net farm losses (**-₹24,804.82**).
4. **Irrigation Efficiency**: Drip Irrigation yields **6.27 tonnes per 1,000 m³**, doubling the efficiency of traditional Flood Irrigation (**3.44 tonnes per 1,000 m³**).

---

## 🚀 How to Run the Project

### 1. Run via Python Script
```bash
python seasonal_agriculture_analysis.py
```
This script will execute the full data cleaning, statistical modeling, and export 8 chart figures to `outputs/charts/`.

### 2. Run via Jupyter Notebook
Open `Seasonal_Agriculture_Performance_Analysis.ipynb` in Jupyter Notebook, JupyterLab, or VS Code and run all cells sequentially.

---

## 👤 Author
- **Author**: Aryan
- **Email**: adaryan543210@gmail.com
- **Program**: VOIS AICTE Batch1 (2026-2027)
