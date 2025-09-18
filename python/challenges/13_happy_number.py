'''Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.


Example 1:

Input: n = 19
Output: true
Explanation:
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1

'''


'''Thoughts

    I will need to calculate the value from digits
    To identify if i am making cycles i will store the values that i passed in a set and if exists in the set it means that i came over a cycle


'''

def calculate_value(n):
    return sum(int(d)*int(d) for d in str(n))

def is_happy_number(n):

    values_seen = set()

    number = calculate_value(n)

    while number not in values_seen:
        values_seen.add(number)
        number = calculate_value(number)

        if number == 1:
            return True
    return False








print(is_happy_number(2))