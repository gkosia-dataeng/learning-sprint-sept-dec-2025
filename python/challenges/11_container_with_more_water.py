'''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

'''

'''Thinking about problem:

        container contains the most water: squate area 
                                                        x: second point position - first point position
                                                        y: min(first point height, second point height)

        i know its a two pointers pattern: somehow i need to convert it to sorted list
        
'''


height = [1,8,6,2,5,4,8,3,7]


l=0
r=len(height) - 1
max_aerea = 0

while l < r :

    x = r-l
    y = min(height[l], height[r])
    max_aerea = max(max_aerea, (x*y))


    if height[r] < height[r]:
        r-=1
    else:
        l+=1

print(max_aerea)

