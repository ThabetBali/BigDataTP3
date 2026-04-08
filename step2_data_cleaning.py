"""
TP03 – Step 2: Data Cleaning & Preprocessing
Reads sales_data.csv, cleans it, and saves sales_data_clean.csv.
Requires: sales_data.csv (run step0_generate_data.py first)
"""

import pandas as pd
import numpy as np
from scipy.stats import zscore

data = pd.read_csv('sales_data.csv')

print("── Step 2: Data Cleaning ──")
print(f"Before: {data.shape[0]} rows | {data.isnull().sum().sum()} missing values | {data.duplicated().sum()} duplicates")

# Drop rows with missing values
data.dropna(inplace=True)

# Remove duplicate rows
data.drop_duplicates(inplace=True)

# Convert date column to datetime
data['date'] = pd.to_datetime(data['date'])

# Remove sales outliers using Z-score
data = data[(np.abs(zscore(data['sales'])) < 3)]

# Add useful time columns
data['month']      = data['date'].dt.month
data['month_name'] = data['date'].dt.strftime('%b')
data['quarter']    = data['date'].dt.quarter

print(f"After:  {data.shape[0]} rows | {data.isnull().sum().sum()} missing values | {data.duplicated().sum()} duplicates")

data.to_csv('sales_data_clean.csv', index=False)
print("✓ sales_data_clean.csv saved")
