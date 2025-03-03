number = 1
times = 0
sum = 0
positive =0
negative =0

print("Please type in integer numbers. Type in 0 to finish.")
while number != 0:
    number = int(input())
    print(f"Number {number}")
    times +=1
    sum +=number
    if number>=1:
        positive +=1
    if number<0:
        negative +=1
    if number ==0:
        print(f"Numbers typed in {times-1}")
        print(f"The sum of the numbers is {sum}" )
        print(f"The mean of the numbers is {sum/(times-1)}")
        print(f"Positive numbers {positive}")
        print(f"Negative numbers {negative}")
        break
        