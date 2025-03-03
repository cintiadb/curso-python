number = int(input("Please type in a number:"))
while number >0:
    if number == 0:
        print("The factorial of the number 0 is 1")
        number = int(input("Please type in a number:"))
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i 
        print(f"The factorial of the number {number} is {factorial}")
        number = int(input("Please type in a number:"))
if number < 0:
    print("Thanks and bye!") 