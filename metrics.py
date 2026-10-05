import pandas as pd

filename = 'Sample - Superstore.csv' 

try:
    df = pd.read_csv(filename, encoding='latin1')
    
    # 1. Total Sales and Total Profit
    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    
    print(f"--- High-Level Business Metrics ---")
    print(f"Total Sales:  ${total_sales:,.2f}")
    print(f"Total Profit: ${total_profit:,.2f}")
    
    # 2. Sales by Region
    print("\n--- Sales by Region ---")
    sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()
    print(sales_by_region)

except Exception as e:
    print(f"An error occurred: {e}")