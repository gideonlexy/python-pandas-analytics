# Import your libraries
import pandas as pd

# OUTPUT:    one row per user_flags record that has NULL in more than one column
# WHO:       each row in user_flags
# METRIC:    count of NULL columns per row
# HIDDEN 1:  strictly > 1, not >= 1
# HIDDEN 2:  no aggregation — row-level null counting only
# FILTER:    none 


# LEVEL 0 — Output
#   grain:      one row per user_flags record with null_count > 1
#   columns:    flag_id, user_firstname, user_lastname, video_id
#   operation:  ISOLATE WHERE null_count > 1; PROJECT (drop null_count from output)

# LEVEL 1 — Label null count per row
#   grain:      one row per user_flags record
#   columns:    all columns + null_count
#  operation:  LABEL null_count = df.isnull().sum(axis=1)

# RAW
#   user_flags: one row per flag record

user_flags.head()
df = user_flags
null_count = df.isnull().sum(axis=1)
mask = null_count > 1
result = df[mask]