'''Challenge: Sessionize User Activity Logs
You are given a stream of user activity logs in the form of a list of dictionaries. Each log contains:

    user_id (string)
    timestamp (ISO 8601 string)
    event (string)

A "session" is defined as a sequence of events from the same user where the gap between consecutive events is no more than 30 minutes.
If the gap is larger, a new session starts.

Task:

Write a Python function that:
    Takes the logs (unsorted list of dicts).
    Groups them into sessions per user.
    Returns a dictionary where the key = user_id and the value = list of sessions.
Each session is a dict with:
    session_id (you can generate a UUID or incrementing counter per user)
    start_time (first event’s timestamp)
    end_time (last event’s timestamp)
    events (list of event names in order)

'''

expected_output = {
    "u1": [
        {
        "session_id": "1",
        "start_time": "2025-08-18 10:00:00",
        "end_time": "2025-08-18 10:10:00",
        "events": ["login", "click"]
        },
        {
        "session_id": "2",
        "start_time": "2025-08-18 11:00:00",
        "end_time": "2025-08-18 11:00:00",
        "events": ["logout"]
        }
    ],
    "u2": [
        {
        "session_id": "1",
        "start_time": "2025-08-18 10:05:00",
        "end_time": "2025-08-18 10:05:00",
        "events": ["login"]
        },
        {
        "session_id": "2",
        "start_time": "2025-08-18 12:00:00",
        "end_time": "2025-08-18 12:00:00",
        "events": ["click"]
        }
    ]
}


logs = [
    {"user_id": "u1", "timestamp": "2025-08-18T10:00:00", "event": "login"},
    {"user_id": "u1", "timestamp": "2025-08-18T10:10:00", "event": "click"},
    {"user_id": "u1", "timestamp": "2025-08-18T11:00:00", "event": "logout"},
    {"user_id": "u2", "timestamp": "2025-08-18T10:05:00", "event": "login"},
    {"user_id": "u2", "timestamp": "2025-08-18T12:00:00", "event": "click"}
]


import pandas as pd
import json

# load to df
df_logs = pd.read_json(json.dumps(logs))

# calculate time of prev log
df_logs["pre_log_record"] = df_logs.groupby("user_id")["timestamp"].shift(1)

# diff from prev log
df_logs["time_from_prev_log"] = (df_logs["pre_log_record"] - df_logs["timestamp"]).dt.total_seconds() / 60

# filter start of sessions and create the timestamp_end
df_sessions_start = df_logs[(df_logs["time_from_prev_log"].isna()) | (df_logs["time_from_prev_log"] < -30 )]
df_sessions_start["timestamp_end"] = df_sessions_start["timestamp"] + pd.Timedelta(minutes=30)

# bind the logs on session start record
df_session_events = pd.merge(df_sessions_start, df_logs,"inner",on="user_id")
df_session_events = df_session_events[(df_session_events["timestamp_x"]<= df_session_events["timestamp_y"]) & (df_session_events["timestamp_end"] >= df_session_events["timestamp_y"])]
print(df_session_events)


# calculate the sessions
df_agg_sessions = df_session_events.groupby(["user_id", "timestamp_x"]).agg(
    end_time =  ("timestamp_y", "max")
    ,events   = ("event_y", list)
).reset_index()

df_agg_sessions["session_id"] = df_agg_sessions.sort_values("timestamp_x").groupby("user_id").cumcount() +1 
df_agg_sessions.rename(columns={"timestamp_x" : "start_time"},inplace=True)
print(df_agg_sessions)

# convert timestamps to string to be serialized 
df_agg_sessions["session_id"] = df_agg_sessions["session_id"].astype(str)
df_agg_sessions["start_time"] = df_agg_sessions["start_time"].astype(str)
df_agg_sessions["end_time"] = df_agg_sessions["end_time"].astype(str)

output = {
    user: group[["session_id","start_time", "end_time", "events"]].to_dict(orient="records")
    for user, group in df_agg_sessions.groupby("user_id")
}

assert expected_output == output, f"Output is not matching, got {output}, expected {expected_output}"

