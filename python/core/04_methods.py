numbers = [1,2,3,4,5,6,7,8,9]
other_numbers = [9,8,7,6,5,4,3,2,1]

double = lambda x: x*2

add = lambda x,y: x+y 

# map(function, iterable): return an iterator ==> add it in list()
print(f"Apply map on list { list(map(double, numbers)) }")

print(f"Apply map on multiple lists { list(map(add, numbers, other_numbers)) }")

# filter

print(f"Apply filter > 3  {list(filter(lambda x: x> 3, numbers))}")