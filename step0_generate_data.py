"""
TP03 – Step 0: Generate Synthetic Sales Dataset
Run this first. Produces sales_data.csv used by all other steps.
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)

n = 500

products   = ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse', 'Headset', 'Webcam']
regions    = ['North', 'South', 'East', 'West']
categories = {
    'Laptop': 'Computers', 'Phone': 'Mobile', 'Tablet': 'Mobile',
    'Monitor': 'Computers', 'Keyboard': 'Accessories',
    'Mouse': 'Accessories', 'Headset': 'Audio', 'Webcam': 'Audio'
}

start_date = datetime(2023, 1, 1)

data = {
    'date':        [start_date + timedelta(days=random.randint(0, 364)) for _ in range(n)],
    'product':     [random.choice(products) for _ in range(n)],
    'region':      [random.choice(regions) for _ in range(n)],
    'quantity':    np.random.randint(1, 20, n),
    'unit_price':  np.random.uniform(20, 1500, n).round(2),
    'customer_id': [f'C{random.randint(1000, 1200)}' for _ in range(n)],
}

df = pd.DataFrame(data)
df['category'] = df['product'].map(categories)
df['sales']    = (df['quantity'] * df['unit_price']).round(2)

# Inject missing values and duplicates to practice cleaning
df.loc[random.sample(range(n), 15), 'sales']  = np.nan
df.loc[random.sample(range(n), 10), 'region'] = np.nan
df = pd.concat([df, df.sample(5)], ignore_index=True)

df.to_csv('sales_data.csv', index=False)

print("✓ sales_data.csv created")
print(f"  Rows: {df.shape[0]}  |  Missing values: {df.isnull().sum().sum()}")
