'''
    Multiline comments
'''

def a_method_with_dockstring(a, b):
    '''This is a dockstring of method a_method_with_dockstring \\
       Is also in description when hover over method name

       To considered dockstring should be the first statement in the method
    '''

    return a+b


print(f"Print method dockstrings {a_method_with_dockstring.__doc__}")