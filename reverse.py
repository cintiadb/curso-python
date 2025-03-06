def everything_reversed(words):
    return [s[::-1] for s in words[::-1]]

my_list = ["Hi", "there", "example", "one more"]
new_list = everything_reversed(my_list)
print(new_list)
