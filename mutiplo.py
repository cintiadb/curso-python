# Write your solution here
number = int(input("Please type in a number: "))
i = 1
multiplo = 0


while True:
    if number > multiplo:
        i * multiplo
        multiplo +=1
        print(f"{i} x {multiplo} = {i*multiplo}")
    elif number == multiplo:
        i+=1
        multiplo = 0
        i * multiplo
        multiplo +=1
        print(f"{i} x {multiplo} = {i*multiplo}")
    if number == i and number == multiplo:
        break
        
    
    
    






