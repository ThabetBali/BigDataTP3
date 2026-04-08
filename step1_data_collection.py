"""
TP03 – Step 1: Data Collection
Loads sales_data.csv and prints a preview.
Requires: sales_data.csv (run step0_generate_data.py first)
"""

import pandas as pd

data = pd.read_csv('sales_data.csv')

print("── Step 1: Data Collection ──")
print(f"Shape: {data.shape}")
print(f"\nFirst 5 rows:")
print(data.head())
print(f"\nColumn types:\n{data.dtypes}")
print(f"\nMissing values:\n{data.isnull().sum()}")
