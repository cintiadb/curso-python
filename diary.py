with open("diary.txt","a+") as my_file:
    text = True
    while text == True:
        function = input("1 - add an entry, 2 - read entries, 0 - quit")
        if function == "1":
            entry = input("Diary entry:")
            my_file.write(entry + "\n")
            my_file.flush()  # Asegura que se guarde inmediatamente
        elif function == "2":
            my_file.seek(0)  # Mueve el puntero al inicio
            content = my_file.read()
            print("Diary entries:\n" + content)
        elif function == "0":
            print("Ok.bye")
            text = False
            break


