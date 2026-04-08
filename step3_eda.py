"""
TP03 – Step 3: Exploratory Data Analysis (EDA)
Produces eda_plots.png with 4 visualizations.
Requires: sales_data_clean.csv (run step2_data_cleaning.py first)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('sales_data_clean.csv', parse_dates=['date'])

print("── Step 3: EDA ──")
print(data[['quantity', 'unit_price', 'sales']].describe().round(2))

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Sales Data – Exploratory Analysis', fontsize=16, fontweight='bold')

# Monthly sales trend
monthly = data.groupby(data['date'].dt.to_period('M'))['sales'].sum().reset_index()
monthly['date'] = monthly['date'].astype(str)
axes[0, 0].plot(monthly['date'], monthly['sales'], marker='o', color='steelblue', linewidth=2)
axes[0, 0].set_title('Monthly Sales Revenue')
axes[0, 0].set_xlabel('Month')
axes[0, 0].set_ylabel('Total Sales (£)')
axes[0, 0].tick_params(axis='x', rotation=45)
axes[0, 0].grid(True, linestyle='--', alpha=0.5)

# Sales by product
top_products = data.groupby('product')['sales'].sum().sort_values(ascending=False)
axes[0, 1].bar(top_products.index, top_products.values, color='coral')
axes[0, 1].set_title('Total Sales by Product')
axes[0, 1].set_xlabel('Product')
axes[0, 1].set_ylabel('Total Sales (£)')
axes[0, 1].tick_params(axis='x', rotation=30)

# Sales by region
region_sales = data.groupby('region')['sales'].sum().sort_values()
region_sales.plot(kind='barh', ax=axes[1, 0], color='mediumpurple')
axes[1, 0].set_title('Sales by Region')
axes[1, 0].set_xlabel('Total Sales (£)')

# Correlation heatmap
corr = data[['quantity', 'unit_price', 'sales', 'month', 'quarter']].corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=axes[1, 1], linewidths=0.5)
axes[1, 1].set_title('Correlation Matrix')

plt.tight_layout()
plt.savefig('eda_plots.png', dpi=150, bbox_inches='tight')
plt.show()
print("✓ eda_plots.png saved")
