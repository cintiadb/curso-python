sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def print_sudoku(sudoku: list):
    for row in sudoku:
        print(" ".join(str(num) if num != 0 else "_" for num in row))

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number


print_sudoku(sudoku)
add_number(sudoku, 0, 0, 2)
add_number(sudoku, 1, 2, 7)
add_number(sudoku, 5, 7, 3)
print()
print("Three numbers added:")
print()
print_sudoku(sudoku)

"""
Hint

Remember it is possible to call the print function without causing a line change:

print("characters ", end="")
print("without carriage returns", end="")
Sample output
characters without carriage returns

Sometimes you need just a new line, which a print statement without any argument will achieve:

print()"
"""