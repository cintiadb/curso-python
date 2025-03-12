def times_ten(start_index: int, end_index: int):
    d = {}
    for item in range (start_index,end_index):
        d[item] = item*10
    return d
        

d = times_ten(3, 6)
print(d)