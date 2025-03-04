items=[]
item = 0
times=int(input("How many items:"))
for n in range(times):
    cosa = int(input(f"Item {n+1}:")) 
    items.append(cosa)
print(items)