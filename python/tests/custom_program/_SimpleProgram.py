def calculate_sum(*args):

    if len(args) == 0:
        raise ValueError("Empty list is passed")

    total = 0
    for i in args:
        total+=i

    return total
