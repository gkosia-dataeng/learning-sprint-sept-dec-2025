'''Iterate over a ***SORTED*** list or array to find pairs or elements that meet a specific criteria


    Problem: Find two numbers in a sorted array that add up to a target value

    Example:
        Input: nums = [1, 2, 3, 4, 6], target = 6
        Output: [1, 3]

    Insights:
        Becasue the list is ***SORTED*** when i move to the left i get a greater number, if i move to the right i am getting a smaller number
        In order to check for specific combination i will iterate with the two pointers from start and end and based on condition i will move the one of the two UNTIL L < R
'''

nums = [1, 2, 3, 4, 6]
target = 6

left_index = 0
right_index = len(nums)-1

while nums[left_index] + nums[right_index] != target:
    if(nums[left_index] + nums[right_index]) > target:
        right_index-=1
    else:
        left_index+=1

print(f"{left_index=}, {right_index=}")