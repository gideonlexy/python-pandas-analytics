# Platform : StrataScratch
# Difficulty : Medium
# Problem Statement : Compare the number of downloads between paying and non-paying customers over time.

# OUTPUT:  one row per date, non_paying_downloads, paying_customer_downloads
# WHO:     date
# METRIC:  SUM downloads split by paying_customer flag per date
# HIDDEN 1: paying_customer is 'yes'/'no' — needs pivot to split into two columns
# HIDDEN 2: filter non_paying > paying applies AFTER aggregation
# FILTER:  none upfront

# LEVEL 0: ISOLATE WHERE non_paying > paying; sort by date ASC
# LEVEL 1: COLLAPSE — groupby date, pivot paying_customer into two columns
# LEVEL 2: ENRICH — merge facts → user_dimension ON user_id
#                          → acc_dimension ON acc_id
# RAW:
#    ms_download_facts:  one row per (date, user_id)
#    ms_user_dimension:  one row per user_id
#    ms_acc_dimension:   one row per acc_id

# Import your libraries
import pandas as pd

# Start writing code

df = pd.merge(ms_user_dimension, ms_download_facts, on='user_id').merge(ms_acc_dimension, on='acc_id')
df = df.groupby(['date', 'paying_customer'])['downloads'].sum().reset_index(name='total_downloads')
df = df.pivot_table(
    index='date',
    columns='paying_customer',
    values= 'total_downloads'
    ).reset_index()
    
df = df.rename(columns={'no': 'non_paying', 'yes':'paying'})

valid = df['non_paying'] > df['paying']
df = df[valid].sort_values('date')