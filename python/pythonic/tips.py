numbers = [1,2,3,4,5,6,7,8,9]

# unpacking
a,b,c = numbers[:3]
print(f"Unpacking {a,b,c}")


# *args
def method_with_args(*args):
    total = 0
    for i in args:
        total+=i 

    return total

print(f"Method with *args {method_with_args(), method_with_args(1,3)}")


# *args
def method_with_kwargs(**kwargs):
    return {k: v for k, v in kwargs.items()}

print(f"Method with **kwargs {method_with_kwargs(), method_with_kwargs(a=1, b=2)}")

# ternary operator
print(f"Use tyernary operator {'Yes' if 4 > 5 else 'No'}")