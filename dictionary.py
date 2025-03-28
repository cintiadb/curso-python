with open("dictionary.txt","a+") as my_file:
    while True:
        function = input("1 - Add word, 2 - Search, 3 - Quit ")
        if function == "1":
            entry1 = input("The word in finnish:")
            entry2 = input("The word in English: ")
            my_file.write(entry1 + "-" + entry2 + "\n")
            my_file.flush() 
        elif function == "2":
            search = input("Search term: ")
            my_file.seek(0)
            for line in my_file:
                if search in line:
                    print(line.strip())  
        elif function == "3":
            print("Ok.bye")
            text = False
            break