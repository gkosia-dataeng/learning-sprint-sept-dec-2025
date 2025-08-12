''' Decorators are used to extend a function without change the inside code of the function
    The decorator function receive in the input the function and wrap it with extra code

'''


def printer_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call the function")
        result = func(*args, **kwargs)
        print("After call the function")
        return result
    return wrapper


@printer_decorator
def add_nums(a,b):
    print(f"Sum is {a+b}")


add_nums(3,4)