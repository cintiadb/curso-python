def spruce(a):
    print("a spruce!")
    for item in range (0,a):
        print(" " * (a - item) + '*' * (2 * item - 1))
    print(" " * (a - 1) + "*")


if __name__ == "__main__":
    spruce(5)