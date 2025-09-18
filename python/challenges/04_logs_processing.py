'''You are given a list of web server log entries in the format: timestamp, user_id, url, response_time_ms

Parse the logs into a structured format (list of dicts, or a pandas DataFrame).
Find the top 2 most visited URLs.
Calculate the average response time per URL.
Find the user who made the most requests.
(Bonus) Detect if any URL had an average response time above 400ms and flag it as “slow”.


Do not use external libraries except pandas or Python standard library.
The solution should be efficient (O(n) or O(n log n) is fine).
'''

logs = """2025-09-01T10:15:23Z,u1,/home,120
2025-09-01T10:15:25Z,u2,/products,250
2025-09-01T10:15:29Z,u1,/products,300
2025-09-01T10:15:33Z,u3,/home,180
2025-09-01T10:15:40Z,u2,/cart,500"""


'''
    Thoghts:
        2 most visited URLs:             count per url
        average response time per URL:   total resp / count
        user who made the most requests: count/user
        if any URL had an average response time above 400ms and flag it as “slow”

'''

# without pandas
logs_list = logs.split('\n')

urls_stats = {'urls': {}, 'users':{}}
most_requests = {'user_id': 0, 'total': 0}

for log in logs_list:
    timestamp, user_id, url, response_time_ms = log.split(',')

    if url not in urls_stats['urls']:
        urls_stats['urls'][url] = {'count': 0, 'total_response': 0, 'is_slow': 0, 'avg_response': 0}

    urls_stats['urls'][url]['count']+=1
    urls_stats['urls'][url]['total_response']+=int(response_time_ms)
    urls_stats['urls'][url]['avg_response'] = urls_stats['urls'][url]['total_response'] / urls_stats['urls'][url]['count']
    urls_stats['urls'][url]['is_slow'] = 0 if  urls_stats['urls'][url]['avg_response'] < 400 else 1
    

    if user_id not in urls_stats['users']:
        urls_stats['users'][user_id] = {'count': 0}

    urls_stats['users'][user_id]['count']+=1

    if most_requests['total'] < urls_stats['users'][user_id]['count']:
        most_requests['total'] = urls_stats['users'][user_id]['count']
        most_requests['user_id'] = user_id


from collections import Counter

cnt = Counter({k: v['count'] for k,v in  urls_stats['urls'].items()} )

print(cnt.most_common(2))
print(urls_stats)
print(most_requests)



# with pandas
import pandas as pd
from io import StringIO

df = pd.read_csv(StringIO(logs),  names=["timestamp", "user_id", "url", "response_time_ms"])
print(df.value_counts('url'))

df_agg = df.groupby("url").agg(
      avg_response = ('response_time_ms', 'mean'),
).reset_index()

df_agg['is_slow'] = (df_agg['avg_response'] > 400).astype(int)
print(df_agg)

print(df.groupby('user_id').agg(cnt = ('user_id', 'count')).sort_values('cnt', ascending=False).head(1))