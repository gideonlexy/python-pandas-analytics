# Problem: Find the last time each bike was used in the first quarter of 2012, and sort the results by the last used time.

# Import your libraries
import pandas as pd

# Start writing code
dc_bikeshare_q1_2012.head()
df = dc_bikeshare_q1_2012
df = df.groupby(['bike_number'])['end_time'].max().reset_index(name='last_used')
df = df.sort_values("last_used")
result = df[['bike_number', 'last_used']]