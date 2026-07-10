# Platform: StataScratch
# Difficulty: Medium
# Problem Statement: Calculate the percentage of shipable orders
    
# OUTPUT:  single scalar — percentage of shipable orders
# WHO:     all orders (no grouping)
# METRIC:  100.0 * COUNT(shipable) / COUNT(all orders)
# HIDDEN 1: shipable = address is not NULL and not empty/whitespace
# HIDDEN 2: orders with no matching customer count in denominator as unshipable
# FILTER:  none

# LEVEL 0: Output
#    grain:     single scalar
#    columns:   shipable_percentage
#    operation: PROJECT ROUND(percentage, 2)

# LEVEL 1: Compute percentage
#    grain:     single row
#    columns:   shipable_count, total_count
#    operation: COLLAPSE — sum(is_shipable) / count(all rows) * 100

# LEVEL 2: Label each order as shipable
#    grain:     one row per order
#    columns:   order_id, address, is_shipable
#    operation: LABEL is_shipable = 1 where address not null/empty else 0

# LEVEL 3: Enrich orders with customer address
#    grain:     one row per order
#    columns:   order_id, cust_id, address
#    operation: ENRICH — LEFT merge orders → customers ON cust_id = customers.id

# RAW:
#    orders:    one row per order
#    customers: one row per customer

# Import your libraries
import pandas as pd

# Start writing code
orders.head()
customers = customers.rename(columns={'id':'cust_id'})
df = pd.merge(orders, customers, on='cust_id', how='left')
df = df[['id', 'cust_id', 'order_date', 'address']]
df['is_shipable'] = df['address'].notnull()
shipable =  df['is_shipable'].sum()
total = len(df)
percentage = shipable / total * 100
result = pd.DataFrame({'percentage': [percentage]})