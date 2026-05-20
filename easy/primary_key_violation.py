# Platform: StrataScratch
# Problem : Find customers who violated the primary key constraint in the dim_customer table. A primary key violation occurs when there are duplicate entries for a unique identifier, such as cust_id in this case. 
# We need to identify customers who have more than one entry in the dim_customer table.

# Import your libraries
import pandas as pd

# Start writing code
dim_customer.head()
df = dim_customer
df = df.groupby('cust_id')['cust_id'].count().reset_index(name='customer_count')
# df = df[df['customer_count'] > 1]
df = df.query('customer_count > 1')