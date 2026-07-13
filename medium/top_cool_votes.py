# Platform: StrataScratch
# Difficulty: Medium
# Problem Statement: Find the review with the highest number of cool votes  

# Import your libraries
import pandas as pd

# Start writing code
yelp_reviews.head()

#method 1
df = yelp_reviews[['business_name', 'review_text', 'cool']]
df['rnk'] = df['cool'].rank(method='dense', ascending=False)
df = df.sort_values('rnk', ascending=False)
top = df[df['rnk'] == 1]
results = top[['business_name', 'review_text' ]]

#method 2
df = yelp_reviews[['business_name', 'review_text', 'cool']]
top = df['cool'] == df['cool'].max()
df = df[top][['business_name', 'review_text']]