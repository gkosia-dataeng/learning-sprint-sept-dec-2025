my_list = [1,2,3,4,5,6]


# dictionary from comprehension
my_dict = {i: i*2 for i in my_list}
print (f"dictionary from comprehension {my_dict}")

# iterate on dictionary
double_value_of_my_dict = {k: v*2 for k,v in my_dict.items()}
print(f"Iterate on dictionary {double_value_of_my_dict}")
