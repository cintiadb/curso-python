sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

def block_correct(sudoku: list, row_no: int, column_no: int):
    row = sudoku[row_no]
    column = row[column_no]
    found_numbers = [False] *9 
    for i in range(3):
        for j in range(3):
            number = sudoku[row_no + i][column_no + j]
            if number != 0:  
                if number < 1 or number > 9 or found_numbers[number - 1]:
                    return False
                found_numbers[number - 1] = True  


    return True  



print(block_correct(sudoku, 0, 0))
print(block_correct(sudoku, 1, 2))

column_no = 1
column = []
for row in sudoku:
    column.append(row[column_no])

for c in column:
    print(c)