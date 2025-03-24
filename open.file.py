with open("numbers.txt") as new_file:
    lista = []
    for line in new_file:
        lista.append(int(line))
def largest():
    print(max(lista))
largest()