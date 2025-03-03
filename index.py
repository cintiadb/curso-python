word = input("Please type in a string: ")
substring = input("Please type a substring: ")

index = word.find(substring)  # Find the first occurrence of the substring
if index != -1:
    second_index = word.find(substring, index + len(substring))  # Find the second occurrence starting after the first one
    if second_index != -1:
        print(f"The second occurrence of the substring is at index {second_index}")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring is not found in the string.")
    