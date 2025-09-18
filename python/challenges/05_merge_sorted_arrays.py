'''
    Median of Two Sorted Arrays

    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
    The overall run time complexity should be O(log (m+n)).

    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.
'''
import logging

logging.basicConfig(level=logging.DEBUG)


# solution is O(M+N)
def mean_of_arrays(lst1, lst2):

    f_index = 0
    s_index = 0

    f_len = len(lst1)
    s_len = len(lst2)

    merged_lst = []
    for i in range(0,(f_len + s_len)):

        if f_index == f_len:
            merged_lst.extend(lst2[s_index:])
            break
        elif s_index == s_len:
            merged_lst.extend(lst1[f_index:])
            break
        elif lst1[f_index] <= lst2[s_index]:
            merged_lst.append(lst1[f_index])
            f_index+=1
        else:
            merged_lst.append(lst2[s_index])
            s_index+=1

    logging.debug(f"Merged list {merged_lst}")
    
    if len(merged_lst)%2 == 0:
        return (merged_lst[int(len(merged_lst)/2)-1] + merged_lst[int(len(merged_lst)/2)]) / 2
    else:
        return merged_lst[int((len(merged_lst)/2))]


print(mean_of_arrays([1,3], [2]))


print(mean_of_arrays([1,2,3,4,5,6,9,10], [2,2,2,5,]))
