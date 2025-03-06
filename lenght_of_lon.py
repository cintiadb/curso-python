def length_of_longest(words):
    return max(len(s) for s in words)


my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = length_of_longest(my_list)
print(result)
