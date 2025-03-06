def distinct_numbers(numbers):
    return sorted(set(numbers))

my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list)) # [1, 2, 3]