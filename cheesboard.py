def chessboard(number):
    for item in range(number):
        numero = ""
        for a in range(number):
            if (item+a) %2 ==0:
                numero +="1"
            else:
                numero +="0"
        print(numero)



# Testing the function
if __name__ == "__main__":
    chessboard(3)
