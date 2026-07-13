# Platform: StartaScratch
# Difficulty: Easy
# Problem Statement: Compare the average popularity of employees by location 

# Import your libraries
import pandas as pd

# Start writing code
facebook_employees.head()
facebook_hack_survey = facebook_hack_survey.rename(columns={'employee_id': 'id'})
df = pd.merge(
    facebook_employees[['id', 'location']],
    facebook_hack_survey[['id', 'popularity']], 
    on='id' )
df = df.groupby(['location'])['popularity'].mean().reset_index(name='avg_pop')
result = df.sort_values('avg_pop', ascending=False)