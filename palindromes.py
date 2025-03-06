def palindromes(word):
    return word == word[::-1]

def main():
    while True:
        user_input = input("Please type in a palindrome: ")
        if palindromes(user_input):
            print(f"{user_input} is a palindrome!")
            break  
        else:
            print("that wasn't a palindrome")

main()