'''Given a string s, find the length of the longest substring without duplicate characters.


    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
'''

input_data = "abcabcbb"
i = 0
max_length = 0
j=0

max_length_i = 0
max_length_j = 0


seen = set()

while j < len(input_data):
    if input_data[j] not in seen:
        seen.add(input_data[j])
        j+=1

        if max_length < j-i:
            max_length_i = i
            max_length_j = j
        max_length = max(max_length, j-i)
    else:
        seen.remove(input_data[i])
        i+=1

print(max_length, input_data[max_length_i:max_length_j])