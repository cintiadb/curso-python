my_list = [1, 2, 3, 4, 5]

def range_of_list(my_list):
    greatest = max(my_list)
    smallest=min(my_list)
    return greatest-smallest

result = range_of_list(my_list)

print("The range of the list is", result)
