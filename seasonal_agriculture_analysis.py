"""
VOIS AICTE Batch1 2026-2027 Major Project: Seasonal Agriculture Performance Analysis
Domain: Agriculture | Theme: Seasonal Agriculture Performance
Tools: Python, Pandas, NumPy, Matplotlib, Seaborn

This script executes the complete data analytics pipeline:
1. Data Ingestion & Quality Analysis
2. Missing Value Imputation & Cleaning
3. Univariate, Bivariate, and Multivariate EDA
4. Outlier Analysis
5. Seasonal Performance Comparison (Kharif vs Rabi vs Zaid)
6. Feature Engineering (Profit Margin %, Total NPK, Cost/Ha, Water Efficiency)
7. Insights & Empirical Findings Generation
8. Exporting High-Resolution Charts to outputs/charts/
"""

import os
import sys
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for server/script execution
import matplotlib.pyplot as plt
import seaborn as sns

# Configure display options and visual themes
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8
pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", lambda x: f"{x:,.2f}")

# Directories setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "seasonal_agriculture_performance_dataset.csv")
CHARTS_DIR = os.path.join(BASE_DIR, "outputs", "charts")
os.makedirs(CHARTS_DIR, exist_ok=True)

print("="*80)
print("VOIS AICTE BATCH1 2026-2027 MAJOR PROJECT")
print("SEASONAL AGRICULTURE PERFORMANCE ANALYSIS")
print("="*80)

# ---------------------------------------------------------
# 1. LOAD DATASET
# ---------------------------------------------------------
if not os.path.exists(DATA_PATH):
    # Fallback to Downloads folder if missing in local dir
    DATA_PATH = r"C:\Users\adary\Downloads\seasonal_agriculture_performance_dataset.csv"

print(f"\n[1] Loading dataset from: {DATA_PATH}")
df = pd.read_csv(DATA_PATH)
print(f"-> Successfully loaded {df.shape[0]} rows and {df.shape[1]} columns.")

# ---------------------------------------------------------
# 2. DATA QUALITY & CLEANING
# ---------------------------------------------------------
print("\n[2] Data Quality Check & Preprocessing")
print(f"-> Initial Duplicate Count: {df.duplicated().sum()}")
df = df.drop_duplicates().reset_index(drop=True)

# Missing values inspection & treatment
missing = df.isnull().sum()
missing_cols = missing[missing > 0]
if len(missing_cols) > 0:
    print("-> Missing values detected:")
    for col, count in missing_cols.items():
        pct = (count / len(df)) * 100
        print(f"   - {col}: {count} missing ({pct:.2f}%)")
        # Impute numeric columns with median by Season and Crop
        if np.issubdtype(df[col].dtype, np.number):
            df[col] = df.groupby(["Season", "Crop"])[col].transform(lambda x: x.fillna(x.median()))
            # If any remain missing, fill overall median
            df[col] = df[col].fillna(df[col].median())
    print("-> Missing values successfully imputed using group median.")
else:
    print("-> No missing values found in the dataset.")

# Data validation checks
df['Revenue_Calculated'] = df['Production_Tonnes'] * df['Market_Price_INR_Tonne']
df['Profit_Calculated'] = df['Revenue_INR'] - df['Total_Cost_INR']

# ---------------------------------------------------------
# 3. FEATURE ENGINEERING
# ---------------------------------------------------------
print("\n[3] Engineering Derived Features...")
df['Profit_Margin_pct'] = np.where(df['Revenue_INR'] > 0, (df['Profit_INR'] / df['Revenue_INR']) * 100, 0)
df['Total_NPK_kg_ha'] = df['Nitrogen_kg_ha'] + df['Phosphorus_kg_ha'] + df['Potassium_kg_ha']
df['Cost_per_Hectare'] = df['Total_Cost_INR'] / df['Farm_Area_Hectares']
df['Revenue_per_Hectare'] = df['Revenue_INR'] / df['Farm_Area_Hectares']
df['Profit_per_Hectare'] = df['Profit_INR'] / df['Farm_Area_Hectares']
df['Water_Per_Hectare'] = df['Water_Used_m3'] / df['Farm_Area_Hectares']

# Categorize Profitability State
df['Profitability_Status'] = np.where(df['Profit_INR'] >= 0, 'Profitable', 'Loss-Making')

print("-> Engineered features: Profit_Margin_pct, Total_NPK_kg_ha, Cost_per_Hectare, Revenue_per_Hectare, Profit_per_Hectare, Profitability_Status.")

# ---------------------------------------------------------
# 4. STATISTICAL SUMMARY BY SEASON
# ---------------------------------------------------------
print("\n[4] Statistical Summary Across Seasons (Kharif, Rabi, Zaid)")
season_stats = df.groupby("Season").agg(
    Farm_Count=('Farm_ID', 'count'),
    Avg_Rainfall_mm=('Rainfall_mm', 'mean'),
    Avg_Temp_C=('Avg_Temperature_C', 'mean'),
    Avg_Humidity_pct=('Humidity_pct', 'mean'),
    Avg_Yield_Tonnes_Ha=('Yield_Tonnes_Ha', 'mean'),
    Total_Production=('Production_Tonnes', 'sum'),
    Avg_Cost=('Total_Cost_INR', 'mean'),
    Avg_Revenue=('Revenue_INR', 'mean'),
    Avg_Profit=('Profit_INR', 'mean'),
    Profitability_Rate=('Profitability_Status', lambda x: (x == 'Profitable').mean() * 100),
    Avg_Water_Efficiency=('Water_Efficiency_t_per_1000m3', 'mean'),
    Avg_Pest_Risk=('Disease_Pest_Risk_pct', 'mean')
).reset_index()

print(season_stats.to_string(index=False))

# ---------------------------------------------------------
# 5. CHARTS GENERATION
# ---------------------------------------------------------
print("\n[5] Generating Visualization Charts...")

# Chart 1: Season Distribution (Pie Chart)
plt.figure(figsize=(7, 7))
season_counts = df['Season'].value_counts()
plt.pie(season_counts, labels=season_counts.index, autopct='%1.1f%%', colors=['#2ca02c', '#1f77b4', '#ff7f0e'], startangle=140, explode=(0.03, 0.03, 0.03))
plt.title('Distribution of Farms Across Seasons', fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "01_season_distribution_pie.png"), dpi=300)
plt.close()

# Chart 2: Yield Distribution across Seasons (Histogram & KDE)
plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='Yield_Tonnes_Ha', hue='Season', kde=True, bins=30, palette='Set2', alpha=0.6)
plt.title('Yield Distribution (Tonnes/Ha) by Season', fontsize=14, fontweight='bold')
plt.xlabel('Yield (Tonnes/Ha)')
plt.ylabel('Farm Count')
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "02_yield_distribution_by_season.png"), dpi=300)
plt.close()

# Chart 3: Environmental Conditions Comparison across Seasons
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
sns.boxplot(data=df, x='Season', y='Rainfall_mm', ax=axes[0, 0], palette='Blues')
axes[0, 0].set_title('Rainfall (mm) by Season', fontweight='bold')

sns.boxplot(data=df, x='Season', y='Avg_Temperature_C', ax=axes[0, 1], palette='YlOrRd')
axes[0, 1].set_title('Average Temperature (°C) by Season', fontweight='bold')

sns.boxplot(data=df, x='Season', y='Humidity_pct', ax=axes[1, 0], palette='Greens')
axes[1, 0].set_title('Humidity (%) by Season', fontweight='bold')

sns.boxplot(data=df, x='Season', y='Sunlight_Hours_Day', ax=axes[1, 1], palette='Oranges')
axes[1, 1].set_title('Sunlight Hours/Day by Season', fontweight='bold')

plt.suptitle('Environmental Parameters Comparison Across Seasons', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "03_environmental_metrics_by_season.png"), dpi=300)
plt.close()

# Chart 4: Economic Performance (Profit, Revenue, Cost) by Season
plt.figure(figsize=(12, 6))
season_econ = df.groupby('Season')[['Total_Cost_INR', 'Revenue_INR', 'Profit_INR']].mean().reset_index()
season_econ_melt = pd.melt(season_econ, id_vars=['Season'], value_vars=['Total_Cost_INR', 'Revenue_INR', 'Profit_INR'], var_name='Financial_Metric', value_name='Amount_INR')
sns.barplot(data=season_econ_melt, x='Season', y='Amount_INR', hue='Financial_Metric', palette='viridis')
plt.title('Average Financial Performance per Farm by Season', fontsize=14, fontweight='bold')
plt.ylabel('Amount (INR)')
plt.ticklabel_format(style='plain', axis='y')
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "04_financial_performance_by_season.png"), dpi=300)
plt.close()

# Chart 5: Crop Yield by Season (Heatmap)
plt.figure(figsize=(10, 6))
crop_season_matrix = df.pivot_table(index='Crop', columns='Season', values='Yield_Tonnes_Ha', aggfunc='mean')
sns.heatmap(crop_season_matrix, annot=True, fmt=".2f", cmap="YlGnBu", linewidths=0.5, cbar_kws={'label': 'Mean Yield (Tonnes/Ha)'})
plt.title('Mean Crop Yield (Tonnes/Ha) Matrix across Seasons', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "05_crop_season_yield_heatmap.png"), dpi=300)
plt.close()

# Chart 6: Water Efficiency by Irrigation Method & Season
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Irrigation_Method', y='Water_Efficiency_t_per_1000m3', hue='Season', palette='mako')
plt.title('Water Efficiency (Tonnes per 1000m³) by Irrigation Method & Season', fontsize=14, fontweight='bold')
plt.xlabel('Irrigation Method')
plt.ylabel('Water Efficiency (t / 1000m³)')
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "06_water_efficiency_irrigation_season.png"), dpi=300)
plt.close()

# Chart 7: Disease & Pest Risk % vs Humidity & Rainfall
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Humidity_pct', y='Disease_Pest_Risk_pct', hue='Season', size='Rainfall_mm', sizes=(20, 200), alpha=0.7, palette='coolwarm')
plt.title('Disease & Pest Risk (%) vs Humidity (%) and Rainfall', fontsize=14, fontweight='bold')
plt.xlabel('Humidity (%)')
plt.ylabel('Disease & Pest Risk (%)')
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "07_pest_risk_vs_humidity.png"), dpi=300)
plt.close()

# Chart 8: Correlation Matrix Heatmap
plt.figure(figsize=(14, 10))
num_cols = ['Farm_Area_Hectares', 'Rainfall_mm', 'Avg_Temperature_C', 'Humidity_pct', 
            'Sunlight_Hours_Day', 'Soil_pH', 'Soil_Moisture_pct', 'Total_NPK_kg_ha', 
            'Fertilizer_kg_ha', 'Pesticide_Litre_ha', 'Yield_Tonnes_Ha', 'Production_Tonnes', 
            'Total_Cost_INR', 'Revenue_INR', 'Profit_INR', 'Water_Efficiency_t_per_1000m3', 'Disease_Pest_Risk_pct']
corr = df[num_cols].corr()
sns.heatmap(corr, annot=False, cmap='coolwarm', vmin=-1, vmax=1, linewidths=0.3)
plt.title('Pearson Correlation Matrix of Agricultural Features', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(CHARTS_DIR, "08_correlation_heatmap.png"), dpi=300)
plt.close()

print(f"-> Generated and saved 8 high-resolution figures in '{CHARTS_DIR}'.")

# ---------------------------------------------------------
# 6. ANSWERS TO KEY QUESTIONS & EVIDENCE SYNTHESIS
# ---------------------------------------------------------
print("\n" + "="*80)
print("EVIDENCE-BASED ANSWERS TO KEY ANALYTICAL QUESTIONS")
print("="*80)

q1_season_yield = df.groupby('Season')['Yield_Tonnes_Ha'].mean()
print(f"\nQ1: How does agricultural yield vary across seasons?")
for season, val in q1_season_yield.items():
    print(f"   - {season}: Mean Yield = {val:.2f} Tonnes/Ha")

q2_season_econ = df.groupby('Season')['Profit_INR'].mean()
print(f"\nQ2: How do economic outcomes (Profit) vary across seasons?")
for season, val in q2_season_econ.items():
    print(f"   - {season}: Mean Profit = INR {val:,.2f}")

q3_best_crop = df.groupby(['Season', 'Crop'])['Profit_INR'].mean().unstack()
print(f"\nQ3: Which crops perform best in each season?")
for season in ['Kharif', 'Rabi', 'Zaid']:
    if season in q3_best_crop.index:
        top_crop = q3_best_crop.loc[season].idxmax()
        top_profit = q3_best_crop.loc[season].max()
        print(f"   - {season}: Best Crop is '{top_crop}' with avg profit of INR {top_profit:,.2f}")

q4_irrigation = df.groupby('Irrigation_Method')['Water_Efficiency_t_per_1000m3'].mean()
print(f"\nQ4: Which irrigation method provides the highest water efficiency?")
for irr, eff in q4_irrigation.items():
    print(f"   - {irr}: {eff:.2f} tonnes / 1000m³")

q5_risk = df.groupby('Season')['Disease_Pest_Risk_pct'].mean()
print(f"\nQ5: How does Disease/Pest Risk vary across seasons?")
for season, risk in q5_risk.items():
    print(f"   - {season}: Mean Pest Risk = {risk:.2f}%")

print("\n" + "="*80)
print("PROJECT EXECUTION COMPLETED SUCCESSFULLY!")
print("="*80)
