'''
    Problem: Calculate the sum of multiple different cases in a list between i,j

    Solution: Preprocess the list and generate a new list in which each item is the sum of all previous points
              
              1. The sum of any sub-array (between j,i) is the prefix[j] - prefix[i-1]
              2. If two positions has the same prefix sum it means that the sum of number between those two positions is 0 (from one point to another we have net 0 )

    Insight: in this way we are calculating once the prefix list and then solve any combination just by deviding 2 points
             
'''



input = [1,3,4,5,-3,-2,8,9]

sum = 0
pre_processed_lst=[]
for num in input:
    sum+=num
    pre_processed_lst.append(sum)


print(pre_processed_lst)


# sum of input[3,7]
print(pre_processed_lst[7] - pre_processed_lst[3-1]) # sum(j) - sum(i-1)

