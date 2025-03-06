
def all_the_longest(words):
    max_length = max(len(s) for s in words)
    return [s for s in words if len(s) == max_length]



my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = all_the_longest(my_list)
print(result)