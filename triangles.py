def triangle(a):
    for item in range (0,a+1):
        result = ('#' * item)
        print(result)

if __name__ == "__main__":
    triangle(6)
    print()
    triangle(3)