list= []
suma =1
print(f"The list is now {list}")
pregunta = input("a(d)d, (r)emove or e(x)it: ")


while True:
    if pregunta == "d":
        list.append(suma)
        suma +=1
        print(f"The list is now {list}")
        pregunta = input("a(d)d, (r)emove or e(x)it:")
    elif pregunta == "r":
        list.pop()
        print(f"The list is now {list}")
        pregunta = input("a(d)d, (r)emove or e(x)it:")
    else:
        print("Bye")
        break



