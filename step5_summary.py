"""
TP03 – Step 5: Project Summary
Prints key metrics and lists files ready for Power BI.
Requires: sales_data_clean.csv and customer_segments.csv
"""

import pandas as pd

data        = pd.read_csv('sales_data_clean.csv')
customers   = pd.read_csv('customer_segments.csv')

top_product = data.groupby('product')['sales'].sum().idxmax()
top_region  = data.groupby('region')['sales'].sum().idxmax()

print("══════════════════════════════════════")
print("TP03 – PROJECT SUMMARY")
print("══════════════════════════════════════")
print(f"Total Revenue    : £{data['sales'].sum():,.2f}")
print(f"Total Orders     : {len(data)}")
print(f"Unique Customers : {data['customer_id'].nunique()}")
print(f"Top Product      : {top_product}")
print(f"Top Region       : {top_region}")

print("\nCustomer segments:")
print(customers.groupby('segment_label')[['total_sales', 'num_orders']].mean().round(2))

print("\nFiles ready for Power BI:")
print("  → sales_data_clean.csv    (main dashboard source)")
print("  → customer_segments.csv   (segmentation layer)")
print("\nSuggested Power BI visuals:")
print("  • Line chart   – monthly sales trend")
print("  • Bar chart    – top products by revenue")
print("  • Map          – sales by region")
print("  • Scatter      – customer segments")
print("  • KPI cards    – total revenue, orders, customers")
