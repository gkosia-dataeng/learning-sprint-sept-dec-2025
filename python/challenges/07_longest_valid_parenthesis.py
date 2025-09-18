'''
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

    Input: s = "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()".
    Example 2:

    Input: s = ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()".
'''
import logging

logging.basicConfig(level=logging.DEBUG)


def longet_valid_parenthesis(input):

    if input == "":
        return 0


    net_count = 0
    max_valid_length = 0
    closed_parenthesis = 0

    for k in input:
        
        if k == "(":
            net_count+=1
        else:
            if net_count >= 1:
                net_count-=1
                closed_parenthesis+=1
            else:
                if closed_parenthesis > max_valid_length:
                    max_valid_length = closed_parenthesis
                    closed_parenthesis= 0
                    net_count = 0

    return max(max_valid_length, closed_parenthesis) * 2


input = ")()())"
print(longet_valid_parenthesis(input))


