#Question:
""" You have a dataset containing information about wines, including their regions, varieties, and prices. 
Some wines have two regions listed (region_1 and region_2). Calculate the total cost of wines for each combination of region and variety, using both region columns.

Because there are two regions listed, first combine the data from both region columns, making sure to remove any duplicate entries and excluding any records with missing prices or regions. 
Then, sum the prices for each unique combination of region and variety and present the results, showing the region, variety, and total price. 
Order the final result from the highest total price to the lowest."""


# Import your libraries
import pandas as pd

# Start writing code
winemag_p1.head()

winemag = winemag_p1[['region_1', 'price', 'variety']]
winemag.rename(columns={'region_1': 'region'}, inplace=True)
winemag2 = winemag_p1[['region_2', 'price','variety']]
winemag2.rename(columns={'region_2': 'region'}, inplace=True)

#concat the two lists
total_dt = pd.concat([winemag, winemag2])

total_dt.shape[0]

#drop duplicates
total_dt = total_dt.drop_duplicates()
#drop rows with where region is null
total_dt = total_dt.dropna(subset=['region'])
#aggregate data by region and variety
total_dt = total_dt.groupby(['region', 'variety'])['price'].sum().reset_index()
total_dt = total_dt[total_dt['price'] > 0]