'''Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1. 
    Input: nums = [0,1,1,1,1,1,0,0,0] 
    Output: 6 
    Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.

'''


'''Thinking about problem:

        1. Find subarray with equal number of 0 and 1
        2. If we change the 0 with -1 then the sum of the elements of sub array = 0
        3. So the problem reduce to find the longest subarray with sum of items = 0 

        4. Calculating the prefix_sum of the array
        5. Theory: If the same prefix_sum occurs at two different indices, the sum of the subarray in between is 0

'''


nums = [0,1,0,1,1,0,0,0,0]
nums_transformed = [-1 if x == 0 else x for x in nums]

prefix_sum = []

# calculate prefix sum
sum = 0
for number in nums_transformed:
    sum+=number
    prefix_sum.append(sum)


index_map = {0: -1}
max_length = 0
print(prefix_sum)
for pos,cumm_sum  in enumerate(prefix_sum):

    if cumm_sum not in index_map:
        index_map[cumm_sum] = pos
    else:
        max_length = max(max_length, pos - index_map[cumm_sum])

print(index_map)


print(max_length)