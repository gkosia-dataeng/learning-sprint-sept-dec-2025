'''First Missing Positive

    Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
    You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

    Input: nums = [1,2,0]
    Output: 3
    Explanation: The numbers in the range [1,2] are all in the array.
'''
import logging

logging.basicConfig(level = logging.DEBUG)

def find_first_missing_positive(lst):
    
    lst_len = len(lst)
    i=0
    tmp = 0

    while i < lst_len:
        if lst[i] == i+1: # if number its in correct position
            i+=1
            continue
        
        if lst[i] > 0 and lst[i] < lst_len:
            tmp = lst[lst[i]-1]
            lst[lst[i]-1] = lst[i]
            lst[i] = tmp
        else:
            i+=1
    
    logging.debug(f"{lst=}")
    for k,v in enumerate(lst):
        if k+1 != v:
            return k+1
    
    
    return lst_len + 1

print(find_first_missing_positive([3, 4, -1, 1]))