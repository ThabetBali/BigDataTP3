"""
TP03 – Step 4: Advanced Analysis – Customer Segmentation (K-Means)
Produces segmentation_plots.png and customer_segments.csv.
Requires: sales_data_clean.csv (run step2_data_cleaning.py first)
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv('sales_data_clean.csv')

print("── Step 4: Customer Segmentation ──")

# Aggregate one row per customer
customer_df = data.groupby('customer_id').agg(
    total_sales    =('sales', 'sum'),
    num_orders     =('sales', 'count'),
    avg_order_value=('sales', 'mean')
).reset_index()

# Scale features
scaler   = StandardScaler()
features = scaler.fit_transform(customer_df[['total_sales', 'num_orders', 'avg_order_value']])

# Elbow method
inertias = []
k_range  = range(2, 8)
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(features)
    inertias.append(km.inertia_)

# Fit with k=3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
customer_df['segment'] = kmeans.fit_predict(features)

# Label clusters by average total_sales
means = customer_df.groupby('segment')['total_sales'].mean().sort_values()
label_map = {means.index[0]: 'Low Value', means.index[1]: 'Mid Value', means.index[2]: 'High Value'}
customer_df['segment_label'] = customer_df['segment'].map(label_map)

print(customer_df.groupby('segment_label')[['total_sales', 'num_orders', 'avg_order_value']].mean().round(2))

# Plots
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle('Customer Segmentation', fontsize=14, fontweight='bold')

axes[0].plot(list(k_range), inertias, marker='o', color='steelblue')
axes[0].axvline(3, color='red', linestyle='--', label='k=3 chosen')
axes[0].set_title('Elbow Method')
axes[0].set_xlabel('Number of Clusters (k)')
axes[0].set_ylabel('Inertia')
axes[0].legend()
axes[0].grid(True, linestyle='--', alpha=0.5)

colors = {'Low Value': '#E24B4A', 'Mid Value': '#378ADD', 'High Value': '#1D9E75'}
for label, color in colors.items():
    mask = customer_df['segment_label'] == label
    axes[1].scatter(
        customer_df.loc[mask, 'num_orders'],
        customer_df.loc[mask, 'total_sales'],
        c=color, label=label, alpha=0.7, s=60
    )
axes[1].set_title('Customers by Segment')
axes[1].set_xlabel('Number of Orders')
axes[1].set_ylabel('Total Sales (£)')
axes[1].legend()
axes[1].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('segmentation_plots.png', dpi=150, bbox_inches='tight')
plt.show()

customer_df.to_csv('customer_segments.csv', index=False)
print("✓ segmentation_plots.png saved")
print("✓ customer_segments.csv saved")
