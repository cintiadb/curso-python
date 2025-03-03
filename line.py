def shape(a,b,c,d):
    for item in range (0,a+1):
        result = (b * item)
        print(result)
    for item in range (c):
        print(d*a)

if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")
