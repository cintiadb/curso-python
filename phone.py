

phone_book = {}

command = input("command(1 search,2 add, 3 quit)")

while True:

    if command == "1":
        name = input("name:")
        if name in phone_book:
            print(phone_book[name])
            print("ok")
        command = input("command(1 search,2 add, 3 quit)")

    elif command =="2":
        name = input("name:")
        number = input("number:")
        phone_book[name] = number
        print ("ok")
        command = input("command(1 search,2 add, 3 quit)")

    if command == "3":
        print("quitting..")
        break