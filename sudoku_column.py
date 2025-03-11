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

def column_correct(sudoku: list, column_no: int):
    column= sudoku[column_no]
    found_numbers = [False] * 9  

    for row in sudoku:
        number = row[column_no]
        if number != 0:  
            if number < 1 or number > 9 or found_numbers[number - 1]:
                return False 
            found_numbers[number - 1] = True  

    return True  

print(column_correct(sudoku, 0))
print(column_correct(sudoku, 1))