'''Slide over an array and find ***continues subarray*** with speficif condition

    Initiate two indexes with difference k
    In each loop subtract the left, add the right
'''


array = [2,3,4,5,6,7,8,9]
k= 3

i = 0
j = k

while j < len(array)+1:
    print(i,j,array[i:j])
    i+=1
    j+=1


# or pythonic 
# zip will stop until all iterables have items (until the shorter length)
print(list(zip(array, array[1:], array[2:])))