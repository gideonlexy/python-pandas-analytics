# Platform: StrataScratch
# Difficulty: Hard
# Problem Statement: Find the top 5 states with the highest number of 5-star businesses 

import pandas as pd

# Start writing code
yelp_business.head()
df = yelp_business[['business_id', 'state','stars']]
five_star = df['stars']  == 5
df = df[five_star]
df = df.groupby('state')['business_id'].count().reset_index(name='business_count')
df = df.sort_values('business_count', ascending=False)
df['rnk'] = df['business_count'].rank(method='dense', ascending=False)
df = df[df['rnk'] <= 5][['state', 'business_count']]
