'''Write a Python function that:
    Parses the logs into structured records (datetime, user, action, status).
    Computes:
        The total number of actions per user.
        The success rate per action type (e.g., "search" = 2/3 success).
        Returns the results in a dictionary of dictionaries.

'''


import logging

logging.basicConfig(level=logging.INFO)

logs = [
    "2025-08-23 12:01:05,user1,search,success",
    "2025-08-23 12:02:10,user2,search,failure",
    "2025-08-23 12:05:55,user1,click,success",
    "2025-08-23 12:06:01,user3,search,success",
    "2025-08-23 12:07:15,user2,click,success",
    "2025-08-23 12:08:00,user1,search,failure"
]

expected_output = {
  "user_stats": {
      "user1": 3,
      "user2": 2,
      "user3": 1
  },
  "action_success_rate": {
      "search": 0.5,
      "click": 1.0
  }
}


'''
        My solution 

'''

# Count per user
# Count per action, success, failure

stats = {
     'user_stats': {}
    ,'action_success_rate': {}
}

for log in logs:
    _, user, action, result = log.split(',')
    logging.debug(f"Processing {user=}, {action=}, {result=}")

    if user in stats['user_stats']:
        stats['user_stats'][user]+=1
    else:
        stats['user_stats'][user]= 1

    if action in stats['action_success_rate']:
        stats['action_success_rate'][action][result]+=1
    else:
        stats['action_success_rate'][action] = {
              'success': 0
             ,'failure': 0
            
        }

        stats['action_success_rate'][action][result] = 1


for action in stats['action_success_rate']:
    stats['action_success_rate'][action] = stats['action_success_rate'][action]['success'] / (stats['action_success_rate'][action]['success'] + stats['action_success_rate'][action]['failure'])


assert stats == expected_output, f"Wrong result, got {stats}, expected is {expected_output}"