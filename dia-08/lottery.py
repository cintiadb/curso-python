import random

def lottery_numbers(amount: int, lower: int, upper: int):
    if amount > (upper - lower + 1):
        raise ValueError("Amount of numbers requested exceeds the available range.")
    
    numbers = random.sample(range(lower, upper + 1), amount)
    return sorted(numbers)  


for number in lottery_numbers(7, 1, 40):
    print(number)
