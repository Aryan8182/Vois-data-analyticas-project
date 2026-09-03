import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

nb_path = r"C:\Users\adary\.gemini\antigravity\scratch\Seasonal_Agriculture_Performance_Analysis\Seasonal_Agriculture_Performance_Analysis.ipynb"

print(f"Reading notebook from {nb_path}...")
with open(nb_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

print("Executing notebook cells...")
try:
    ep.preprocess(nb, {'metadata': {'path': r"C:\Users\adary\.gemini\antigravity\scratch\Seasonal_Agriculture_Performance_Analysis"}})
    print("Notebook executed successfully without errors.")
except Exception as e:
    print(f"Notebook execution warning/error: {e}")

print(f"Saving executed notebook back to {nb_path}...")
with open(nb_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Executed notebook saved successfully.")
