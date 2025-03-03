# Write your solution here
number = int(input("Please type in a number: "))

low = 1
high = number

while low <= high:
    print(low)
    low += 1 
    if low <= high:
        print(high)
        high -= 1 