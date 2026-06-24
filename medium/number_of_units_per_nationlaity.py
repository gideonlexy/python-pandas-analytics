## Platform: StrataScratch
## Difficulty: Medium
## Problem Statement: Compare the number of units per nationality

# Import your libraries
import pandas as pd

# Start writing code
airbnb_hosts.head()
df = pd.merge(airbnb_hosts, airbnb_units, on='host_id')
age = df['age'] < 30
unit = df['unit_type'] == 'Apartment'
df = df[(age) & (unit)]
df = df.groupby(['nationality'])['unit_id'].nunique().reset_index(name='counts')
results = df