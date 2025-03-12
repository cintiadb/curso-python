phone_book = {}

command = input("command(1 search,2 add, 3 quit)")

while True:

    if command == "1":
        name = input("name:")
        if name in phone_book:
            print("\n".join(phone_book[name]))  # Print all numbers for the contact
            print("ok")
        else:
            print("no number")
            print("ok")
        command = input("command(1 search,2 add, 3 quit)")

    elif command =="2":
        name = input("name:")
        number = input("number:")
        if name not in phone_book:
            phone_book[name] = [] 
        
        phone_book[name].append(number) 
        print ("ok")
        command = input("command(1 search,2 add, 3 quit)")

    if command == "3":
        print("quitting..")
        break