def read_input():
    while True:
        try:
            input_str = input("Please type in a number: ")
            number = int(input_str)
            if number >=5 and number <=10:
                return number
        except ValueError:
            pass 

        print("You must type in an integer between 5 and 10")


number = read_input()
print("You typed in:", number)