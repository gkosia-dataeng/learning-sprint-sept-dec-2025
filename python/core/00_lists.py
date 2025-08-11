numbers = [1,2,3,4,5,6,7,8,9]

# slising: start(inclusive):end(exclusive):step
# slising: same works in 
print(f"first three: {numbers[0:3]}")
print(f"reverse {numbers[::-1]}")
print(f"reverse using method {list(reversed(numbers))}")
print(f"Latest {numbers[-1]}")
print(f"4th from end until end {numbers[-4:]}")

numbers[:3] = [11,22,33]
print(f"Change multiple items at once {numbers}")



# list comprehensions 
print(f"List comprehensions {[i * 2 for i in  numbers]}")
print(f"List comprehensions with condition{[i * 2 for i in numbers if i  > 5]}")

# zip list
users = ["a", "b", "c"]
ids = [1,2,3]

print(f"nested for using comprehensions {[(x,y) for x in users for y in ids]}")