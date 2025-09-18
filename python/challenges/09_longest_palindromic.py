'''
    Given a string s, return the longest palindromic substring in s.

    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.
'''

input = 'abcdeedfgralllla'


# my solution O(n**3)
def find_largest_palindromic(input):

    for length in range(len(input), 1, -1):
        for i in range(0,int(len(input) - length)):
            if input[i:length + i + 1] == input[i:length + i + 1][::-1]:
                print(input[i:length + i + 1], input[i:length + i + 1][::-1], len(input[i:length + i + 1]))
                return


find_largest_palindromic(input)
