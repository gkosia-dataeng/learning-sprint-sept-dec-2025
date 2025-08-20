'''
    Rules (SCD Type 2):
        If a user is new → insert a new row with valid_from = today, valid_to = None.
        
        If a user exists but attributes changed 
            → Close the old record by setting its valid_to = today.
              Insert a new record with valid_from = today, valid_to = None.

        If no changes → do nothing.
'''
import logging
logging.basicConfig(level=logging.DEBUG)

users_current_state = [
                        {"user_id": "u1", "name": "Alice", "country": "US", "valid_from": "2024-01-01", "valid_to": None},
                        {"user_id": "u2", "name": "Bob",   "country": "UK", "valid_from": "2024-02-01", "valid_to": None},
                     ]

latest_updates = [
                    {"user_id": "u1", "name": "Alice", "country": "CA"},   # country changed
                    {"user_id": "u3", "name": "Eve",   "country": "AU"}    # new user
                ]


expected_output = [
        {"user_id": "u1", "name": "Alice", "country": "US", "valid_from": "2024-01-01", "valid_to": "2025-08-20"},
        {"user_id": "u1", "name": "Alice", "country": "CA", "valid_from": "2025-08-20", "valid_to": None},
        {"user_id": "u2", "name": "Bob",   "country": "UK", "valid_from": "2024-02-01", "valid_to": None},
        {"user_id": "u3", "name": "Eve",   "country": "AU", "valid_from": "2025-08-20", "valid_to": None},
    ]


from typing import List, Dict


'''
    When user found and has change     ---> Expire the current row, Insert new row
    When user found and has not change ---> do nothing
    When user not found                ---> Insert new row
'''

'''
    My solution
'''

def processed_current_row(users_dim: List[Dict[str, any]], user_change: Dict[str, any], date: str) -> bool:
    '''
        Compare the user_change against the dim list

        Return True if the downstream will need to add a current row (user does not exists, user exists and has change)
    '''
    insert_new_record = True

    for user_row in users_dim:
        if user_row['user_id'] == user_change['user_id'] and user_row['valid_to'] == None:
            if has_changes(user_row, user_change):
                user_row['valid_to'] = date
                insert_new_record = True
                break
            else:
                insert_new_record = False
                break
    
    return insert_new_record


def has_changes(dim_user: Dict[str, any], change_user: Dict[str,any]) -> bool:
    
    if dim_user['country'] != change_user['country']:
        return True
    
    return False



def scd_type2(dim: List[Dict], updates: List[Dict], today: str) -> List[Dict]:
    
    for update_row in updates:
        if processed_current_row(dim, update_row, today):
            update_row['valid_from'] = today
            update_row['valid_to'] = None
            dim.append(update_row)
    
    return dim
            


output = scd_type2(users_current_state, latest_updates,"2025-08-20")



def dict_list_equal(l1, l2):
    return {frozenset(d.items()) for d in l1} == {frozenset(d.items()) for d in l2}


assert dict_list_equal(output, expected_output), f"Output does not match, got {output}, expected {expected_output}"



'''
    Chatgbt solution
'''

def scd_type2(dim: List[Dict[str, Any]], updates: List[Dict[str, Any]], today: str) -> List[Dict[str, Any]]:
    # Create a lookup for current active records
    dim_lookup = {row["user_id"]: row for row in dim if row["valid_to"] is None}

    new_dim = dim.copy()  # start with existing dimension table

    for update in updates:
        uid = update["user_id"]
        current = dim_lookup.get(uid)

        if current is None:
            # New user → insert
            new_row = update.copy()
            new_row["valid_from"] = today
            new_row["valid_to"] = None
            new_dim.append(new_row)
        else:
            # Existing user → check for changes
            changed = False
            for key in update:
                if key != "user_id" and current.get(key) != update[key]:
                    changed = True
                    break

            if changed:
                # Close old record
                current["valid_to"] = today

                # Insert new record
                new_row = update.copy()
                new_row["valid_from"] = today
                new_row["valid_to"] = None
                new_dim.append(new_row)
            # else: no changes → do nothing

    return new_dim