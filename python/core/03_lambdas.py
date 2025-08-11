# a lamba function contains only one expression

l_func = lambda x,y,z: x+y+z
print(f"simple lambda {l_func(1,2,3)}")

# using lambda as parameters
names  = ['aaaa', 'bb', 'c']
names.sort()
print(f"Native sort {names}")
names.sort(key = lambda x: len(x))
print(f"Custom logic sort {names}")