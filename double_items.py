def double_items(numbers: list):
    numbers_double = []
    for item in numbers:
        numbers_double.append(item * 2)  # Append the doubled value to the list
    return numbers_double  
        

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)