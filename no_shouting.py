pruned_list=[]

def no_shouting(string):
    for item in my_list:
        if not item.isupper():
            pruned_list.append(item)
    return pruned_list


my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
pruned_list = no_shouting(my_list)
print(pruned_list)