# Problem : Spam Posts
# Platform : StrataScratch

# OUTPUT:   one row per day with percentage of spam view events
# WHO:      post_date
# METRIC:   100.0 * COUNT(is_spam) / COUNT(*) per day — view events not distinct posts
# HIDDEN 1: is_spam uses str.contains — case insensitive match on 'spam'
# HIDDEN 2: COUNT(is_spam) ignores NULLs — ELSE None in CASE WHEN is the mechanism
# HIDDEN 3: grain is one row per view event — no dedup, each view counts separately
# FILTER:   none

# LEVEL 0: Output
#    grain:     one row per post_date
#    columns:   post_date, percentage
#    operation: PROJECT

# LEVEL 1: Collapse to daily spam percentage
#    grain:     one row per post_date
#    columns:   post_date, percentage
#    operation: COLLAPSE — groupby post_date
#               percentage = 100.0 * sum(is_spam) / count(is_spam + non-spam)

# LEVEL 2: Label spam flag per view event row
#    grain:     one row per (post_id, viewer_id)
#    columns:   post_id, post_date, keyword, is_spam
#    operation: LABEL is_spam = 1 where keyword contains 'spam' else 0

# LEVEL 3: Enrich posts with view events
#    grain:     one row per (post_id, viewer_id)
#    columns:   post_id, post_date, keyword
#    operation: ENRICH — merge facebook_posts → facebook_post_views on post_id

# RAW:
#    facebook_posts:      one row per post (post_id, post_date, post_keywords)
#    facebook_post_views: one row per view event (post_id, viewer_id)

# Import your libraries
import pandas as pd

# Start writing code
facebook_posts.head()
df = pd.merge(facebook_posts,facebook_post_views, on='post_id' )
df['is_spam'] = df['post_keywords'].str.contains('spam')
df = df[['post_id', 'post_date','is_spam']]
df = df.groupby(['post_date']).agg(posts=('is_spam', 'sum'),total=('is_spam', 'count')).reset_index()
df['percentage'] = df['posts'] / df['total'] * 100
df[['post_date','percentage']]