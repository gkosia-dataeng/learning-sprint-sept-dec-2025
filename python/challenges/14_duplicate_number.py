'''Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
    There is only one repeated number in nums, return this repeated number.
    You must solve the problem without modifying the array nums and using only constant extra space.

    Input: nums = [1,3,4,2,2]    
    Output: 2

    Input: nums = [3,1,3,4,2]
    Output: 3
'''

'''
    if i have n numbers i will have all numbers except 1 
    In the place of missing number will be the repeated number

    array is not sorted 
    i cannot modify the array
    i cannot use a set to store what i have seen because it requires constant extra space

    its fast/slow pointers problem


'''


def find_duplicate(nums):

    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break


    slow = nums[0]    

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow



nums = [1,3,4,2,2]
print(find_duplicate(nums))